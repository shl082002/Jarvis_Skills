import { useState } from "react";
import { ExplainPanel } from "../components/ExplainPanel";
import { LiveFallback } from "../components/LiveFallback";
import { RunGrid } from "../components/RunGrid";
import { INK } from "../lib/ink";
import type { CockpitState } from "../types";

export function RunsPage({ state }: { state: CockpitState }) {
  const [explainId, setExplainId] = useState<string | null>(null);
  const runs = state.runs ?? [];
  return (
    <div className="mx-auto max-w-[96rem] space-y-[1.6vh] pb-[4vh]">
      {explainId ? <ExplainPanel runId={explainId} onClose={() => setExplainId(null)} /> : null}
      <section className={`${INK.panel} p-[1.6vw]`}>
        <p className={`mb-[1.2vh] text-[0.65rem] uppercase tracking-[0.16em] ${INK.accent}`}>Runs</p>
        {runs.length ? <RunGrid runs={runs} onExplain={setExplainId} /> : <LiveFallback agents={state.live} />}
      </section>
    </div>
  );
}
