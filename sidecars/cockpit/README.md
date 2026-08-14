# Cockpit — Mission Control

Portable kit face. FastAPI projects the target `.jarvis/` workroom.
Doctrine stays Markdown. **Task / AgentRun / Event / Approval** live in
`.jarvis/control.db` (SQLite, created on first serve). TRACKER.md is generated
from Tasks. React draws Mission Control (Command / Signal / Atelier by occasion).

```bash
<path-to-kit>/bin/cockpit open
# http://127.0.0.1:3847/
```

Do **not** put an HTTP `health:` URL on the cockpit service in `services.yml` —
compose uses TCP-only so the worker cannot deadlock on itself.

Check in a run:

```bash
curl -sS -X POST http://127.0.0.1:3847/api/live/beat \
  -H 'content-type: application/json' \
  -d '{"id":"jarvis","role":"assistant","mission":"cockpit slice","phase":"build","status":"running"}'
```
