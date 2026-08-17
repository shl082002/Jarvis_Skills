import { useState } from "react";
import { HiOutlineBolt, HiOutlineCheckCircle, HiOutlineMinusCircle, HiOutlineXCircle } from "react-icons/hi2";
import { postJson } from "../lib/api";
import { INK } from "../lib/ink";
import type { AgentRun } from "../types";

function statusIcon(status: string) {
  if (status === "failed" || status === "stopped") return HiOutlineXCircle;
  if (status === "done") return HiOutlineCheckCircle;
  return HiOutlineBolt;
}

export function RunGrid({
  runs,
  onExplain,
}: {
  runs: AgentRun[];
  onExplain: (id: string) => void;
}) {
  const [busy, setBusy] = useState<string | null>(null);
  const [err, setErr] = useState("");
  if (!runs.length) {
    return (
      <p className={`flex items-center gap-[0.5vw] text-[0.9rem] italic ${INK.dim}`}>
        <HiOutlineMinusCircle className="h-[1.1rem] w-[1.1rem]" />
        No check-ins
      </p>
    );
  }
  return (
    <div>
      {err ? <p className={`mb-[0.8vh] text-[0.65rem] ${INK.wait}`}>{err}</p> : null}
      <div className="grid gap-[1vh] md:grid-cols-2">
        {runs.map((run) => {
          const live = run.status === "queued" || run.status === "running";
          const Glyph = statusIcon(run.status);
          return (
            <article key={run.id} className={`rounded-[0.5rem] border ${INK.line} px-[0.9vw] py-[1.2vh]`}>
              <div className="flex items-center justify-between gap-[0.8vw]">
                <h3 className="flex items-center gap-[0.5vw] font-semibold tracking-wide uppercase">
                  <Glyph className="h-[1.1rem] w-[1.1rem]" />
                  {run.agent_id}
                </h3>
                <span className={`text-[0.65rem] uppercase tracking-wider ${INK.mute}`}>{run.status}</span>
              </div>
              <p className={`mt-[0.4vh] text-[0.7rem] uppercase tracking-wider ${INK.accent}`}>
                {run.phase} {run.task_id ? `· ${run.task_id}` : ""}
              </p>
              <p className="mt-[0.8vh] text-[0.9rem]">{run.mission || "—"}</p>
              <div className="mt-[1.2vh] flex flex-wrap gap-[0.6vw]">
                <button
                  type="button"
                  onClick={() => onExplain(run.id)}
                  className={`rounded-[0.35rem] border ${INK.line} px-[0.8vw] py-[0.4vh] text-[0.65rem] uppercase tracking-wider ${INK.mute}`}
                >
                  Explain
                </button>
                <button
                  type="button"
                  disabled={!live || busy === run.id}
                  onClick={() => {
                    setBusy(run.id);
                    setErr("");
                    void postJson(`/api/runs/${run.id}/stop`, {})
                      .catch((e: Error) => setErr(e.message))
                      .finally(() => setBusy(null));
                  }}
                  className={`rounded-[0.35rem] border ${INK.line} px-[0.8vw] py-[0.4vh] text-[0.65rem] uppercase tracking-wider ${INK.mute} disabled:opacity-40`}
                >
                  Stop
                </button>
              </div>
            </article>
          );
        })}
      </div>
    </div>
  );
}
