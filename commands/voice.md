---
description: Local voice transport — read inbox as chat; speak a one-line wrap only if POLICY voice is on.
---

Apply `skills/voice/SKILL.md`.

- If `WORKROOM/inbox/utterance.md` is new, treat it as the principal’s words
  (same modes, same command words). Then archive/ignore until the next file.
- Do not auto-run qa/build from a homophone.
- TTS: `bin/voice-say` for one line, and only when POLICY has `voice: on`.
