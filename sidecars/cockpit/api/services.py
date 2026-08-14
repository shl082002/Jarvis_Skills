"""HAPPY via bin/svc. Registry names only — no arbitrary shell."""
from __future__ import annotations

import re
import socket
import subprocess
from pathlib import Path

NAME_RE = re.compile(r"^[A-Za-z0-9_-]+$")


def _svc_bin(workroom: Path) -> Path:
    return workroom / "bin" / "svc"


def _names(workroom: Path) -> list[str]:
    registry = workroom / "services.yml"
    if not registry.is_file():
        return []
    names: list[str] = []
    for line in registry.read_text(encoding="utf-8", errors="replace").splitlines():
        if re.match(r"^[A-Za-z0-9_-]+:\s*$", line):
            names.append(line.split(":", 1)[0])
    return names


def _field(workroom: Path, name: str, key: str) -> str:
    registry = workroom / "services.yml"
    if not registry.is_file():
        return ""
    in_s = False
    for line in registry.read_text(encoding="utf-8", errors="replace").splitlines():
        if re.match(rf"^{re.escape(name)}:\s*$", line):
            in_s = True
            continue
        if in_s and re.match(r"^[A-Za-z0-9_-]+:\s*$", line):
            break
        if in_s:
            m = re.match(rf"^\s+{re.escape(key)}:\s*(.*)$", line)
            if m:
                return m.group(1).strip()
    return ""


def _port_listening(port: str) -> bool:
    try:
        p = int(port)
    except ValueError:
        return False
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.3)
    try:
        sock.connect(("127.0.0.1", p))
        return True
    except OSError:
        return False
    finally:
        sock.close()


def _run(workroom: Path, args: list[str], timeout: int) -> tuple[int, str]:
    binary = _svc_bin(workroom)
    if not binary.is_file():
        return 127, "svc not installed in this workroom"
    try:
        result = subprocess.run(
            [str(binary), *args],
            capture_output=True,
            text=True,
            timeout=timeout,
        )
    except subprocess.TimeoutExpired:
        return 124, "svc timed out"
    text = (result.stdout or "") + (result.stderr or "")
    return result.returncode, text.strip()


def list_services(workroom: Path, *, tcp_only: bool = False) -> dict:
    """tcp_only: never HTTP-health (avoids deadlock when compose runs inside the worker)."""
    names = _names(workroom)
    if not names:
        return {"items": [], "note": "Nothing registered — greenfield."}
    if tcp_only:
        items = []
        for name in names:
            port = _field(workroom, name, "port")
            up = _port_listening(port) if port else False
            status = "up" if up else "down"
            items.append(
                {
                    "name": name,
                    "status": status,
                    "detail": f"{name} {status} :{port} (tcp)",
                }
            )
        return {"items": items, "ok": True, "raw": "tcp-only"}
    code, text = _run(workroom, ["status"], timeout=8)
    items = []
    for name in names:
        status = "unknown"
        for line in text.splitlines():
            if name in line.split():
                if "UP" in line:
                    status = "up"
                elif "DOWN" in line:
                    status = "down"
                elif "LISTENING" in line:
                    status = "listening"
                else:
                    status = "unknown"
                break
        items.append({"name": name, "status": status, "detail": ""})
    for item in items:
        for line in text.splitlines():
            if item["name"] in line:
                item["detail"] = line.strip()
                break
    return {"items": items, "ok": code == 0, "raw": text[:2000]}


def control(workroom: Path, name: str, action: str) -> dict:
    if not NAME_RE.match(name) or name not in _names(workroom):
        raise ValueError("unknown service")
    if action not in {"up", "down", "restart"}:
        raise ValueError("action must be up, down, or restart")
    timeout = 90 if action != "down" else 30
    code, text = _run(workroom, [action, name], timeout=timeout)
    return {"ok": code == 0, "output": text[:4000], **list_services(workroom, tcp_only=True)}
