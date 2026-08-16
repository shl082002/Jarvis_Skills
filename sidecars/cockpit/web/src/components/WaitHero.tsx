import { useState } from "react";
import { Mark } from "./Mark";
import { INK } from "../lib/ink";
import type { ControlTask } from "../types";

export function WaitHero({ task }: { task: ControlTask }) {
  const [busy, setBusy] = useState(false);
  const [err, setErr] = useState("");
  const act = (path: string) => {
    setBusy(true);
    setErr("");
    void fetch(path, { method: "POST" })
      .then((res) => {
        window.dispatchEvent(new Event("jarvis-refresh"));
        if (!res.ok) {
          return res.text().then((text) => {
            throw new Error(text.slice(0, 240) || res.statusText);
          });
        }
      })
      .catch((e: Error) => setErr(e.message))
      .finally(() => setBusy(false));
  };
  return (
    <section className={`${INK.panel} col-span-full border-[#f5a524]/40 p-[1.6vw]`}>
      <p className={`mb-[0.8vh] flex items-center gap-[0.5vw] text-[0.65rem] uppercase tracking-[0.16em] ${INK.wait}`}>
        <Mark kind="wait" />
        WAITING_FOR_USER
      </p>
      <h2 className="text-[1.15rem] font-semibold">
        {task.id} · {task.title}
      </h2>
      <p className={`mt-[0.8vh] text-[0.9rem] ${INK.mute}`}>{task.next_action || "A decision is required. Jarvis will not guess."}</p>
      {err ? <p className={`mt-[1vh] text-[0.65rem] ${INK.wait}`}>{err}</p> : null}
      <div className="mt-[1.6vh] flex flex-wrap gap-[0.6vw]">
        <button
          type="button"
          disabled={busy}
          onClick={() => act(`/api/tasks/${task.id}/resume`)}
          className="rounded-[0.4rem] bg-[#7aa2ff] px-[1vw] py-[1vh] text-[0.65rem] font-semibold uppercase tracking-wider text-[#0b0e14]"
        >
          Resume
        </button>
        <button
          type="button"
          disabled={busy}
          onClick={() => act(`/api/tasks/${task.id}/not-now`)}
          className={`rounded-[0.4rem] border ${INK.line} px-[1vw] py-[1vh] text-[0.65rem] uppercase tracking-wider ${INK.mute}`}
        >
          Not now
        </button>
      </div>
    </section>
  );
}
