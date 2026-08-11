---
name: judgment-library
description: On-demand engineering/product judgment cards — teach one topic, cite a law in a design debate, never always-on. Use when asked to teach a concept, which law applies, or "open the handbook".
---

# Judgment Library — one card at a time

Process is the charter. This corpus is **physics**: reliability, scale, data,
APIs, frontend laws. Open **one** topic when judgment is needed. Not always-on.
Not a substitute for verify-live.

## Resolve the library root (first hit wins)

1. `.jarvis/kit/assets/learning/` (installed kit)
2. Kit checkout `assets/learning/` (when working inside the kit repo)
3. Path in `WORKROOM/POLICY.md` (`judgment_library: …`)
4. `./learning/` at the project root

If none exist: say so. Do not invent topics.

## When to open

| Trigger | Action |
|---------|--------|
| `teach` / "teach me …" / "what law is …" | Teach loop |
| DISCUSS architecture | Cite 1–2 **canonical** topics |
| BUILD touching money, events, consistency, realtime | Read named topics before locking |
| Standing ruling after an incident | Memory **pointer** only — never paste the essay |

Otherwise leave it closed.

## Teach loop

1. Open `CONCEPT-INDEX.md` if present — prefer **canonical** over **lens**.
2. Load **one** topic `.md` only.
3. Answer the four questions **against the current product** (ignore travel/Nykaa examples unless asked):
   - What problem does it solve?
   - What happens if we ignore it?
   - Where would we use it here?
   - When must we **not** use it?
4. One short simulation on this codebase or PRD. Stop.

Do not binge the module. Next card only if the principal asks.

## Citing

Chronicle/plan: topic path or id. Chat: conclusion first, topic id as receipt.
