---
description: Capture a durable memory — one fact, one file, indexed. Args: the thing to remember.
---

Save the given fact using `skills/memory/SKILL.md`:

1. Classify it: user | feedback | project | reference. If it's something the
   repo already records, ask what was non-obvious about it and save THAT.
2. Check `.jarvis/MEMORY.md` for an existing file that covers it — update that
   file instead of duplicating.
3. Otherwise write `.jarvis/memory/<kebab-slug>.md` with frontmatter
   (name, description, type), the fact, **Why:**, **How to apply:** (for
   feedback/project), and [[links]] to related memories. Absolute dates only.
4. Add its one-line hook to `.jarvis/MEMORY.md`.
5. Confirm to the principal in one line what was saved and under which name.
