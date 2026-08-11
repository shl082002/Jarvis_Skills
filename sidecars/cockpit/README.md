# Cockpit — living board

Portable kit face. FastAPI reads the **target** `.jarvis/` workroom.
React draws it. No database. Voice is not in this slice.

```bash
# from a project that has .jarvis/
<path-to-kit>/bin/cockpit open
# http://127.0.0.1:3847/
```

Live panel shows `live/<id>.json` only. Missing or older than 90s → unknown.
Check in:

```bash
curl -sS -X POST http://127.0.0.1:3847/api/live/beat \
  -H 'content-type: application/json' \
  -d '{"id":"jarvis","role":"assistant","mission":"cockpit slice","phase":"build","status":"running"}'
```
