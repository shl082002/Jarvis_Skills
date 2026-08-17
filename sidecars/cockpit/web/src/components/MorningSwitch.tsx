import { useState } from "react";
import { postJson } from "../lib/api";
import { INK } from "../lib/ink";

export function MorningSwitch({
  on,
  hour,
  minute,
  errText,
}: {
  on: boolean;
  hour: number;
  minute: number;
  errText?: string;
}) {
  const [busy, setBusy] = useState(false);
  const [err, setErr] = useState("");
  const flip = (next: boolean) => {
    setBusy(true);
    setErr("");
    void postJson("/api/morning-open", { on: next, hour, minute })
      .then((body: { last_error?: string; on?: boolean }) => {
        if (body.last_error) setErr(body.last_error);
      })
      .catch((e: Error) => setErr(e.message))
      .finally(() => setBusy(false));
  };
  const clock = `${String(hour).padStart(2, "0")}:${String(minute).padStart(2, "0")}`;
  return (
    <div className="flex flex-col items-end gap-[0.2vh]">
      <div className={`flex items-center gap-[0.5vw] rounded-full border ${INK.line} p-[0.15vh]`}>
        <span className={`px-[0.6vw] text-[0.6rem] uppercase tracking-wider ${INK.mute}`}>
          Morning {clock}
        </span>
        <button
          type="button"
          disabled={busy || !on}
          onClick={() => flip(false)}
          className={`rounded-full px-[0.8vw] py-[0.4vh] text-[0.65rem] uppercase tracking-wider sm:text-[0.7rem] ${
            !on ? "bg-[#6b7385] text-[#0b0e14]" : `${INK.mute} hover:text-[#e8edf7]`
          }`}
        >
          Off
        </button>
        <button
          type="button"
          disabled={busy || on}
          onClick={() => flip(true)}
          className={`rounded-full px-[0.8vw] py-[0.4vh] text-[0.65rem] uppercase tracking-wider sm:text-[0.7rem] ${
            on ? "bg-[#3dd68c] text-[#0b0e14]" : `${INK.mute} hover:text-[#e8edf7]`
          }`}
        >
          On
        </button>
      </div>
      {err || errText ? <p className={`max-w-[40vw] text-[0.6rem] ${INK.wait}`}>{err || errText}</p> : null}
    </div>
  );
}
