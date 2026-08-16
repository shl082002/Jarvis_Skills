import { useState } from "react";
import { postJson } from "../lib/api";
import { INK } from "../lib/ink";

const MODES = ["discuss", "plan", "build"] as const;

export function ModeSwitch({ current }: { current: string }) {
  const [busy, setBusy] = useState(false);
  const [err, setErr] = useState("");
  return (
    <div className="flex flex-col items-end gap-[0.2vh]">
      <div className={`flex rounded-full border ${INK.line} p-[0.15vh]`}>
        {MODES.map((gear) => (
          <button
            key={gear}
            type="button"
            disabled={busy}
            onClick={() => {
              setBusy(true);
              setErr("");
              void postJson("/api/mode", { mode: gear })
                .catch((e: Error) => setErr(e.message))
                .finally(() => setBusy(false));
            }}
            className={`rounded-full px-[0.9vw] py-[0.4vh] text-[0.65rem] uppercase tracking-wider sm:text-[0.7rem] ${
              current === gear ? "bg-[#7aa2ff] text-[#0b0e14]" : `${INK.mute} hover:text-[#e8edf7]`
            }`}
          >
            {gear}
          </button>
        ))}
      </div>
      {err ? <p className={`max-w-[40vw] text-[0.6rem] ${INK.wait}`}>{err}</p> : null}
    </div>
  );
}
