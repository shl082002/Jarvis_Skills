# Optional `$B` daemon (not the default)

Cursor MCP is the default (`SKILL.md`). Use this only when the principal
wants a **persistent headed Chromium** they can watch (`$B connect`).

**Never** clone or commit gstack inside a product repo. Binary stays outside
the kit tree (typical: `~/gstack/browse/dist/browse`).

## One-time setup (outside the product)

```bash
git clone <gstack-upstream> ~/gstack   # not inside the project
cd ~/gstack && bun install && bun run build
```

Point `$B` at the built CLI. `bin/browse-env` prints an export if it finds
a known location.

## Pre-flight (steal: connect steps 0–2 only)

1. Source `browse-env` or export `B` yourself.
2. If a stale daemon pidfile exists **outside** the product (e.g.
   `~/.gstack/browse.json` or `~/gstack/.gstack/browse.json`), kill that pid
   and remove the json. Do not create `.gstack/` inside the product.
3. Drop Chromium profile locks if a crash left them:
   `~/.gstack/chromium-profile/Singleton{Lock,Socket,Cookie}`.
4. `$B connect` — headed window. Confirm the command’s own output; do not
   invent “connected.”
5. Drive with `$B snapshot` / click / screenshot. Copy screenshots into
   `WORKROOM/evidence/`.

If `$B` is missing, say so and use Cursor MCP. Do not download a binary
into `Jarvis_Skills/`.
