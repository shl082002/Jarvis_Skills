import { useEffect, useState } from "react";
import { INK } from "../lib/ink";

export function ExplainPanel({ runId, onClose }: { runId: string; onClose: () => void }) {
  const [text, setText] = useState("…");
  useEffect(() => {
    let cancelled = false;
    void fetch(`/api/runs/${runId}/explain`)
      .then((r) => r.json())
      .then((body: { summary?: string; detail?: string }) => {
        if (!cancelled) {
          setText(body.summary || body.detail || JSON.stringify(body));
        }
      })
      .catch(() => {
        if (!cancelled) setText("Could not load explain.");
      });
    return () => {
      cancelled = true;
    };
  }, [runId]);
  return (
    <section className={`${INK.panel} col-span-full border-[#7aa2ff]/40 p-[1.6vw]`}>
      <div className="flex items-start justify-between gap-[1vw]">
        <div>
          <p className={`mb-[0.8vh] text-[0.65rem] uppercase tracking-[0.16em] ${INK.accent}`}>Explain</p>
          <p className="text-[0.9rem]">{text}</p>
        </div>
        <button
          type="button"
          onClick={onClose}
          className={`rounded-[0.35rem] border ${INK.line} px-[0.8vw] py-[0.4vh] text-[0.65rem] uppercase tracking-wider ${INK.mute}`}
        >
          Close
        </button>
      </div>
    </section>
  );
}
