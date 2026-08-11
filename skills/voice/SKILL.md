---
name: voice
description: Local voice transport — STT into the workroom inbox, optional TTS. Modes still bind. Use when the principal speaks a command or asks Jarvis to speak a wrap.
---

# Voice — transport, not authorization

Speech is another way to put words into the same loop. It does **not**
create BUILD permission beyond the words themselves. DISCUSS words still
do not launch builders. Do not auto-run `qa` because STT heard “test.”

## Inbox (STT)

Push-to-talk v1. No wake word.

1. Capture text locally (type, or a local Whisper you installed).
2. `bin/voice-inbox` writes `WORKROOM/inbox/utterance.md`.
3. Treat that file like chat: same command words, same sanitization.
4. No cloud STT.

## Speak (TTS)

`bin/voice-say` uses macOS `say(1)`. Silent unless `WORKROOM/POLICY.md`
contains `voice: on`. Default is off.

On wrap, one short line — not the report. Full findings stay in files.

## Never

Cloud STT/TTS in v1 · inventing a second brain · treating a garbled
transcript as a push grant · starting EDITH because a homophone sounded
like “verify.”
