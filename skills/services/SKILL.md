---
name: services
description: The service registry — one file that knows how every local service starts, plus the svc butler script that wakes/sleeps/checks them. Use when starting or stopping the local stack, diagnosing a port conflict or boot failure, or when a new service joins the project.
---

# The Service Registry

Daily dev burns real time on the same ritual: start five services, chase a
port, wonder which env profile is live. This skill replaces the ritual with
one registry file and one command — and gives the workshop's Ops Butler
(HAPPY, `agents/happy.md`) his muscle.

## The pieces

- **`.jarvis/services.yml`** — the registry. One entry per runnable service:
  where it lives, how it starts, which port it owns, how to know it's healthy.
- **`.jarvis/bin/svc`** — the butler script (installed by the kit):
  `svc list | status [name] | up <name>|all | down <name>|all | restart <name> | lights on|off | logs <name> [n]`

**Lights:** `svc lights on` / `svc lights off` is the whole registry, **including Mission Control (`cockpit` :3847)**. HAPPY must not skip the board on a house sleep. The face still refuses to Down itself; HAPPY stops it via svc.
- **`.jarvis/logs/<name>.log`** + **`.jarvis/run/<name>.pid`** — captured
  output and launch pids for everything svc starts.

## Registry format (strict — svc parses it with awk, not a YAML library)

```yaml
service-name:
  dir: path/relative/to/workspace/root
  cmd: single shell command, run from dir, backgrounded, logs captured
  stop: optional command run instead of pid-kill (docker compose stop, etc.)
  port: 8000
  health: http://localhost:8000/health   # optional; TCP port check otherwise
  wait: 60                               # optional boot budget in seconds
  notes: free text — contested ports, env requirements, sharp edges
```

Two-space indent, `key: value`, nothing fancier. Keep `cmd` a SINGLE
command (env prep belongs in the service's own .env or in absolute-path
binaries like `venv/bin/uvicorn`), so signals reach the real process.

## The laws

1. **Status before up.** Act on observed state, never assumption.
2. **UP = health check passed.** A living pid with a failing health URL is
   LISTENING, not UP — report it that way.
3. **Never kill a process you can't name.** svc refuses to down a port
   listener running outside the service's own directory; a contested port
   is a report, not a kill.
4. **Contested ports are registry knowledge.** When two services share a
   port by design (only one runs at a time), say so in both `notes:` lines.
5. **No schedulers without the principal's explicit grant.** The registry
   makes wake/sleep one command; WHEN that command runs stays a human
   decision unless the principal rules otherwise.
6. **The registry is maintained like the ledger.** New service, changed
   port, new env requirement → the registry changes in the same session,
   and at day-close it must match reality.

## Bootstrapping a project

1. Sweep the repos for runnable services (README, package.json scripts,
   docker-compose, uvicorn entry points) — the Scout agent does this well.
2. Cross-check OPERATIONAL truth against repo defaults: the port a service
   actually runs on in this house may differ from its README (the ledger
   and the principal know best).
3. Write `.jarvis/services.yml`; `svc list` + `svc status` to sanity-check.
4. Verify live: cycle one safe service through `up` → healthy → `down`.
