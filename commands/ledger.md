---
description: Update the git branch ledger — record current branches, tips, stack order, push state, verified against git.
---

Update `.jarvis/LEDGER.md` per `skills/git-ledger/SKILL.md`:

1. Per repo: `git branch -v`, `git log --oneline` on working branches,
   `git ls-remote` for any push-state claims.
2. Record/update: today's dated entry — branch, tip hash, base, contents
   one-liner, stack order, push state, live-tree note.
3. Append corrections (❌ CORRECTION) for anything the ledger claimed that git
   disproves — never silently rewrite.
4. Report to the principal: any branch not in the ledger, any ledger claim git
   contradicts, current stack tips per repo.
