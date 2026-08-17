"""Telegram sidecar — kit Mission Control remote. Stdlib only. Bind 127.0.0.1."""
from __future__ import annotations

import json
import os
import socket
import threading
import time
import urllib.error
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

PORT = int(os.environ.get("TELEGRAM_HEALTH_PORT", "3848"))
MC = os.environ.get("MISSION_CONTROL_URL", "http://127.0.0.1:3847")
POLL_SECONDS = 50
POLL_HTTP_TIMEOUT = 70
SEND_HTTP_TIMEOUT = 12
BOARD_TICK = 0.4


def workroom() -> Path:
    env = os.environ.get("JARVIS_WORKROOM", "")
    if env:
        return Path(env).expanduser()
    here = Path(__file__).resolve()
    for parent in here.parents:
        if (parent / "control.db").exists() or (parent / "HANDOVER.md").exists():
            return parent
    return Path.cwd()


def load_env(wr: Path) -> dict[str, str]:
    out: dict[str, str] = {}
    path = wr / ".env"
    if not path.is_file():
        return out
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, val = line.split("=", 1)
        out[key.strip()] = val.strip().strip('"').strip("'")
    return out


def api(path: str, method: str = "GET", body: dict | None = None) -> dict:
    data = None if body is None else json.dumps(body).encode()
    req = urllib.request.Request(
        f"{MC}{path}",
        data=data,
        method=method,
        headers={"content-type": "application/json"} if body is not None else {},
    )
    try:
        with urllib.request.urlopen(req, timeout=8) as res:
            raw = res.read().decode("utf-8", errors="replace")
            return json.loads(raw) if raw else {}
    except urllib.error.HTTPError as exc:
        try:
            raw = exc.read().decode("utf-8", errors="replace")
            parsed = json.loads(raw) if raw else {}
            if isinstance(parsed, dict):
                parsed.setdefault("ok", False)
                return parsed
        except (json.JSONDecodeError, OSError):
            pass
        return {"ok": False}
    except (urllib.error.URLError, OSError, TimeoutError, json.JSONDecodeError):
        return {"ok": False}


def tg(token: str, method: str, payload: dict | None = None, *, http_timeout: float = SEND_HTTP_TIMEOUT) -> dict:
    url = f"https://api.telegram.org/bot{token}/{method}"
    data = json.dumps(payload or {}).encode()
    req = urllib.request.Request(url, data=data, method="POST")
    req.add_header("content-type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=http_timeout) as res:
            return json.loads(res.read().decode())
    except urllib.error.HTTPError as exc:
        try:
            return json.loads(exc.read().decode())
        except (json.JSONDecodeError, OSError):
            return {"ok": False, "description": f"http {exc.code}"}
    except (socket.timeout, TimeoutError, urllib.error.URLError, OSError, json.JSONDecodeError) as exc:
        return {"ok": False, "description": type(exc).__name__}


def same_chat(left: str, right: str) -> bool:
    a, b = left.strip(), right.strip()
    if a == b:
        return True
    try:
        return int(a) == int(b)
    except ValueError:
        return False


def send(token: str, chat: str, text: str) -> bool:
    body = tg(token, "sendMessage", {"chat_id": chat, "text": text[:3500]})
    if not body.get("ok"):
        print(f"telegram: send failed — {body.get('description', body)}", flush=True)
        return False
    return True


class Health(BaseHTTPRequestHandler):
    def log_message(self, fmt: str, *args: object) -> None:
        return

    def do_GET(self) -> None:
        body = b'{"ok":true,"service":"telegram"}'
        self.send_response(200)
        self.send_header("content-type", "application/json")
        self.send_header("content-length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def serve_health() -> None:
    httpd = ThreadingHTTPServer(("127.0.0.1", PORT), Health)
    httpd.serve_forever()


def glance(state: dict) -> str:
    waiting = state.get("waiting") or {}
    g = state.get("gauntlet") or {}
    wait_line = ""
    if waiting:
        wait_line = (
            f"WAITING {waiting.get('id')} · {waiting.get('title')}\n"
            f"{waiting.get('next_action') or 'A decision is required.'}\n"
            "Reply in English. “Not now” parks it.\n"
        )
    return (
        f"Mission Control\n"
        f"{wait_line}"
        f"mode {state.get('mode')} · occasion {state.get('occasion')}\n"
        f"gauntlet {'ON' if g.get('on') else 'OFF'}\n"
        f"watching {state.get('watching')}"
    )


PARK_PHRASES = frozenset({"not now", "notnow", "park", "later", "skip", "hold"})


def is_park_phrase(text: str) -> bool:
    t = text.strip().lower().rstrip(".!")
    return t in PARK_PHRASES


def handle_plain(token: str, chat: str, text: str) -> None:
    state = api("/api/state")
    waiting = state.get("waiting") or {}
    tid = str(waiting.get("id") or "")
    if not tid:
        send(token, chat, "Nothing waiting. I’ll ping when the fleet needs a ruling.")
        return
    park = is_park_phrase(text)
    out = api(f"/api/tasks/{tid}/answer", "POST", {"text": text[:2000], "park": park})
    if not out.get("ok"):
        send(token, chat, "Couldn’t record that. Try once more.")
        return
    if park:
        send(token, chat, f"Parked {tid}. Fleet will stand down that slice.")
        return
    live = any(
        str(r.get("status") or "") in {"queued", "running"}
        for r in (state.get("runs") or [])
    )
    if live:
        send(
            token,
            chat,
            f"Logged on {tid}. Fleet is in motion — Jarvis takes this when that turn stops.",
        )
        return
    send(
        token,
        chat,
        f"Logged on {tid}. House is idle — there is no automatic beat. "
        "Tap the Jarvis chat in Cursor once and he will take the ruling.",
    )


def handle_command(token: str, chat: str, text: str) -> None:
    cmd = text.strip().split()[0].lower().split("@", 1)[0]
    parts = text.strip().split()
    if cmd in {"/status", "/start"}:
        send(token, chat, glance(api("/api/state")))
        return
    if cmd == "/gauntlet" and len(parts) >= 2:
        on = parts[1].lower() in {"on", "1", "true"}
        api("/api/gauntlet", "POST", {"on": on, "reason": "telegram"})
        send(token, chat, f"Gauntlet {'ON' if on else 'OFF'}")
        return
    send(
        token,
        chat,
        "When something is WAITING, reply in English. “Not now” parks it. /status for a glance.",
    )


def watch_board(token: str, chat: str) -> None:
    last_wait = ""
    last_g = None
    while True:
        state = api("/api/state")
        waiting = state.get("waiting")
        wait_key = f"{waiting.get('id')}:{waiting.get('updated_at')}" if waiting else ""
        if wait_key and wait_key != last_wait:
            send(token, chat, glance(state))
            last_wait = wait_key
        if not wait_key:
            last_wait = ""
        gon = bool((state.get("gauntlet") or {}).get("on"))
        if last_g is not None and gon != last_g:
            send(token, chat, f"Gauntlet {'ON' if gon else 'OFF'}")
        last_g = gon
        time.sleep(BOARD_TICK)


def poll_inbound(token: str, chat: str) -> None:
    offset = 0
    while True:
        body = tg(
            token,
            "getUpdates",
            {
                "offset": offset,
                "timeout": POLL_SECONDS,
                "allowed_updates": ["message", "edited_message"],
            },
            http_timeout=POLL_HTTP_TIMEOUT,
        )
        if not body.get("ok"):
            desc = str(body.get("description") or "poll empty")
            if desc not in {"poll empty", "TimeoutError", "timeout", "URLError"}:
                print(f"telegram: getUpdates — {desc}", flush=True)
                time.sleep(1)
            continue
        for upd in body.get("result") or []:
            offset = int(upd.get("update_id", 0)) + 1
            msg = upd.get("message") or upd.get("edited_message") or {}
            from_id = str((msg.get("chat") or {}).get("id") or "")
            text = str(msg.get("text") or "")
            if not from_id:
                continue
            if not same_chat(from_id, chat):
                print("telegram: ignored message from a different chat (check TELEGRAM_CHAT_ID)", flush=True)
                continue
            if text.startswith("/"):
                handle_command(token, chat, text)
            elif text:
                handle_plain(token, chat, text)


def main() -> None:
    wr = workroom()
    env = {**os.environ, **load_env(wr)}
    token = env.get("TELEGRAM_BOT_TOKEN", "").strip()
    chat = env.get("TELEGRAM_CHAT_ID", "").strip()
    threading.Thread(target=serve_health, daemon=True).start()
    print(f"telegram: health 127.0.0.1:{PORT} workroom {wr}", flush=True)
    if not token or not chat:
        print("telegram: waiting for TELEGRAM_BOT_TOKEN + TELEGRAM_CHAT_ID in workroom .env", flush=True)
        while True:
            time.sleep(30)
            env = {**os.environ, **load_env(wr)}
            token = env.get("TELEGRAM_BOT_TOKEN", "").strip()
            chat = env.get("TELEGRAM_CHAT_ID", "").strip()
            if token and chat:
                break
    me = tg(token, "getMe", {})
    if not me.get("ok"):
        print(f"telegram: getMe failed — {me.get('description', me)}", flush=True)
    else:
        print(f"telegram: bot @{me.get('result', {}).get('username', '?')}", flush=True)
    threading.Thread(target=watch_board, args=(token, chat), daemon=True).start()
    print("telegram: inbound long-poll + board tick", flush=True)
    poll_inbound(token, chat)


if __name__ == "__main__":
    main()
