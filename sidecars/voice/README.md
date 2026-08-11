# Voice sidecar (v1)

Transport only. Modes still bind. No cloud STT/TTS.

| Direction | v1 |
|-----------|-----|
| STT | Push-to-talk → text into `WORKROOM/inbox/utterance.md` |
| TTS | macOS `say(1)` via `bin/voice-say` |

Optional local models (not bundled): MLX Whisper or whisper.cpp. If you
transcribe, pipe the text through `bin/voice-inbox` — do not treat the
audio file as a command.

**Default off.** Set `voice: on` in `WORKROOM/POLICY.md` before TTS speaks.
Inbox writes are always allowed (files are untrusted input, same as chat).

Hard rules: `skills/voice/SKILL.md`.
