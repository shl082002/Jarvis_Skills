---
description: Reconcile the code atlas against the real file tree — adds, removals, retags (CURRENT/LEGACY/DEPRECATED/INFRA).
---

Run the atlas reconcile procedure from `skills/atlas/SKILL.md`:

1. Locate the atlas file(s) (per the handover's "where everything is" section;
   default `.jarvis/ATLAS.md`). If none exists, offer to scaffold one from the
   current tree.
2. Diff the actual file tree against the atlas: new, deleted, moved
   dirs/modules.
3. Propose per-delta actions: add (with status tag + one-line purpose), remove,
   retag, or update `replaced-by:` pointers. Verify tags against code, not
   against other documents (delegate the sweep to U where the team exists).
4. Apply approved changes; stamp the reconcile date at the top of the atlas.
5. Report: what drifted, what held, in a short list.
