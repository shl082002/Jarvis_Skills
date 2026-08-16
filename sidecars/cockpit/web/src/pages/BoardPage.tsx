import { useState } from "react";
import { CreateTask } from "../components/CreateTask";
import { ExplainPanel } from "../components/ExplainPanel";
import { LiveFallback } from "../components/LiveFallback";
import { Mark } from "../components/Mark";
import { RunGrid } from "../components/RunGrid";
import { ServiceBoard } from "../components/ServiceBoard";
import { TaskList } from "../components/TaskList";
import { WaitHero } from "../components/WaitHero";
import { MixMeter } from "../components/MixMeter";
import { Pipeline } from "../components/Pipeline";
import { INK, MIX, OCCASION_COPY } from "../lib/ink";
import type { CockpitState } from "../types";

function Stat({
  label,
  value,
  mark,
}: {
  label: string;
  value: string | number;
  mark?: "eye" | "pulse" | "wait" | "bridge" | "signal" | "check";
}) {
  return (
    <div className={`${INK.panel} px-[0.9vw] py-[1.1vh]`}>
      <p className={`flex items-center gap-[0.4vw] text-[0.6rem] uppercase tracking-wider ${INK.mute}`}>
        {mark ? <Mark kind={mark} className="h-[0.85rem] w-[0.85rem]" /> : null}
        {label}
      </p>
      <p className="mt-[0.3vh] truncate text-[1.05rem] font-semibold">{value}</p>
    </div>
  );
}

export function BoardPage({ state }: { state: CockpitState }) {
  const [explainId, setExplainId] = useState<string | null>(null);
  const tasks = state.tasks ?? [];
  const now = tasks.filter((t) => t.lane === "now");
  const awaiting = tasks.filter((t) => t.lane === "awaiting");
  const parked = tasks.filter((t) => t.lane === "parked");
  const next = tasks.filter((t) => t.lane === "next");
  const done = tasks.filter((t) => t.lane === "done").slice(0, 8);
  const runs = state.runs ?? [];
  const fleet = state.fleet ?? [];
  const liveRuns = runs.filter((r) => r.status === "queued" || r.status === "running");
  const services = state.service_board?.items ?? [];
  const occasion = state.occasion ?? "away";
  const copy = OCCASION_COPY[occasion] ?? OCCASION_COPY.away;

  return (
    <div className="mx-auto max-w-[96rem] space-y-[1.6vh] pb-[4vh]">
      {explainId ? <ExplainPanel runId={explainId} onClose={() => setExplainId(null)} /> : null}

      {state.waiting ? <WaitHero task={state.waiting} /> : null}

      <section className={`${INK.panel} p-[1.6vw]`}>
        <p className={`mb-[0.8vh] flex items-center gap-[0.5vw] text-[0.65rem] uppercase tracking-[0.16em] ${INK.accent}`}>
          <Mark kind={copy.mark} />
          {copy.title} · {copy.emotion}
        </p>
        <p className="text-[0.95rem]">{copy.need}</p>
        <p className={`mt-[0.8vh] text-[0.75rem] ${INK.mute}`}>
          Mix recipe: {MIX[occasion] ?? MIX.away}
        </p>
        <div className="mt-[1vh]">
          <MixMeter occasion={occasion} />
        </div>
        <div className="mt-[1.4vh] flex flex-wrap items-center gap-[1vw]">
          <Pipeline mode={state.mode} running={liveRuns.length} waiting={Boolean(state.waiting)} />
          <span className={`rounded-full border ${INK.line} px-[0.8vw] py-[0.4vh] text-[0.65rem] uppercase ${INK.mute}`}>
            {state.mode}
          </span>
          <span className={`rounded-full border ${INK.line} px-[0.8vw] py-[0.4vh] text-[0.65rem] uppercase ${INK.mute}`}>
            {liveRuns.length} running
          </span>
        </div>
        <p className={`mt-[1vh] text-[0.9rem] ${INK.mute}`}>{state.next_task || "No next task on the handover."}</p>
        {state.dispatch ? (
          <p className={`mt-[0.8vh] text-[0.75rem] ${INK.wait}`}>
            Dispatch {state.dispatch.action} · {state.dispatch.agent_id}
            {state.dispatch.task_id ? ` · ${state.dispatch.task_id}` : ""} · {state.dispatch.mission}
          </p>
        ) : null}
      </section>

      <div className="grid grid-cols-2 gap-[0.8vh] sm:grid-cols-3 lg:grid-cols-6">
        <Stat mark="eye" label="Watching" value={state.watching} />
        <Stat mark="bridge" label="Mode" value={state.mode} />
        <Stat mark="signal" label="Gauntlet" value={state.gauntlet?.on ? "on" : "off"} />
        <Stat mark="pulse" label="Live runs" value={liveRuns.length} />
        <Stat mark="wait" label="Awaiting" value={awaiting.length} />
        <Stat mark="check" label="Kit" value={state.kit_health?.status || "—"} />
      </div>

      <div className="grid gap-[1.6vh] lg:grid-cols-3">
        <section className={`${INK.panel} p-[1.4vw]`}>
          <p className={`mb-[0.8vh] flex items-center gap-[0.4vw] text-[0.65rem] uppercase tracking-[0.16em] ${INK.accent}`}>
            <Mark kind="eye" />
            Now · {now.length}
          </p>
          <TaskList tasks={now} empty="Nothing in NOW." fleet={fleet} mode={state.mode} />
          <CreateTask />
        </section>
        <section className={`${INK.panel} p-[1.4vw]`}>
          <p className={`mb-[0.8vh] flex items-center gap-[0.4vw] text-[0.65rem] uppercase tracking-[0.16em] ${INK.wait}`}>
            <Mark kind="wait" />
            Awaiting · {awaiting.length}
          </p>
          <TaskList tasks={awaiting} empty="Nothing awaiting." fleet={fleet} mode={state.mode} />
          {next.length ? (
            <div className="mt-[1.2vh]">
              <p className={`mb-[0.6vh] text-[0.6rem] uppercase ${INK.dim}`}>Next queue</p>
              <TaskList tasks={next} empty="" fleet={fleet} mode={state.mode} />
            </div>
          ) : null}
        </section>
        <section className={`${INK.panel} p-[1.4vw]`}>
          <p className={`mb-[0.8vh] flex items-center gap-[0.4vw] text-[0.65rem] uppercase tracking-[0.16em] ${INK.dim}`}>
            <Mark kind="void" />
            Parked · {parked.length}
          </p>
          <TaskList tasks={parked} empty="Nothing parked." fleet={fleet} mode={state.mode} />
        </section>
      </div>

      <section className={`${INK.panel} p-[1.4vw]`}>
        <p className={`mb-[1vh] flex items-center gap-[0.4vw] text-[0.65rem] uppercase tracking-[0.16em] ${INK.accent}`}>
          <Mark kind="pulse" />
          Fleet · {runs.length} runs · {state.live.length} live beats
        </p>
        {runs.length ? <RunGrid runs={runs} onExplain={setExplainId} /> : <LiveFallback agents={state.live} />}
      </section>

      <div className="grid gap-[1.6vh] lg:grid-cols-2">
        <section className={`${INK.panel} p-[1.4vw]`}>
          <p className={`mb-[0.8vh] flex items-center gap-[0.4vw] text-[0.65rem] uppercase tracking-[0.16em] ${INK.ok}`}>
            <Mark kind="check" />
            Recently done
          </p>
          <TaskList tasks={done} empty="No closed tasks yet." fleet={fleet} mode={state.mode} />
        </section>
        <section className={`${INK.panel} p-[1.4vw]`}>
          <p className={`mb-[0.8vh] flex items-center gap-[0.4vw] text-[0.65rem] uppercase tracking-[0.16em] ${INK.accent}`}>
            <Mark kind="bridge" />
            Services
          </p>
          <ServiceBoard items={services} note={state.service_board?.note} />
        </section>
      </div>

      <div className="grid gap-[1.6vh] lg:grid-cols-2">
        <section className={`${INK.panel} p-[1.4vw]`}>
          <p className={`mb-[0.8vh] text-[0.65rem] uppercase tracking-[0.16em] ${INK.mute}`}>Reports</p>
          {state.reports?.length ? (
            <ul className="space-y-[0.5vh] text-[0.8rem]">
              {state.reports.slice(0, 8).map((r) => (
                <li key={r.name} className="flex justify-between gap-[1vw]">
                  <span className="truncate">{r.name}</span>
                  <span className={INK.dim}>{r.mtime ? r.mtime.slice(0, 16) : "—"}</span>
                </li>
              ))}
            </ul>
          ) : (
            <p className={`italic ${INK.dim}`}>No reports yet.</p>
          )}
        </section>
        <section className={`${INK.panel} p-[1.4vw]`}>
          <p className={`mb-[0.8vh] text-[0.65rem] uppercase tracking-[0.16em] ${INK.mute}`}>Branches · kit health</p>
          <p className="text-[0.85rem]">
            {state.kit_health?.stale ? "STALE" : state.kit_health?.status || "—"}
            {state.kit_health?.beat_fresh_seconds != null
              ? ` · beat window ${state.kit_health.beat_fresh_seconds}s`
              : ""}
          </p>
          {state.branches?.length ? (
            <ul className={`mt-[0.8vh] space-y-[0.3vh] text-[0.8rem] ${INK.mute}`}>
              {state.branches.slice(0, 8).map((b) => (
                <li key={b}>{b}</li>
              ))}
            </ul>
          ) : (
            <p className={`mt-[0.6vh] italic ${INK.dim}`}>No branch ledger lines.</p>
          )}
        </section>
      </div>
    </div>
  );
}
