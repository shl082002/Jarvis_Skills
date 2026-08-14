import { useState } from "react";
import type { AgentRun, ControlTask, LiveAgent, ServiceItem } from "./types";
import { useCockpit } from "./useCockpit";

const MODES = ["discuss", "plan", "build"] as const;
const INK = {
  mute: "text-[#8b95a8]",
  dim: "text-[#6b7385]",
  line: "border-[#243044]",
  panel: "rounded-xl border border-[#243044] bg-[#121722]",
  accent: "text-[#7aa2ff]",
  ok: "text-[#3dd68c]",
  wait: "text-[#f5a524]",
};

type Mark =
  | "eye"
  | "pulse"
  | "wait"
  | "check"
  | "void"
  | "fail"
  | "bridge"
  | "signal"
  | "atelier";

function Icon({ kind, className = "h-4 w-4" }: { kind: Mark; className?: string }) {
  const sw = 1.6;
  return (
    <svg className={className} viewBox="0 0 24 24" fill="none" aria-hidden>
      {kind === "eye" && (
        <>
          <ellipse cx="12" cy="12" rx="8" ry="5" stroke="currentColor" strokeWidth={sw} />
          <circle cx="12" cy="12" r="2.2" fill="currentColor" />
        </>
      )}
      {kind === "pulse" && (
        <path
          d="M3 12h4l2-5 3 10 2-5h7"
          stroke="currentColor"
          strokeWidth={sw}
          strokeLinecap="round"
          strokeLinejoin="round"
        />
      )}
      {kind === "wait" && (
        <>
          <circle cx="12" cy="12" r="8" stroke="currentColor" strokeWidth={sw} />
          <path d="M12 7v5l3 2" stroke="currentColor" strokeWidth={sw} strokeLinecap="round" />
        </>
      )}
      {kind === "check" && (
        <>
          <circle cx="12" cy="12" r="8" stroke="currentColor" strokeWidth={sw} />
          <path d="M8 12.5l2.5 2.5L16 9" stroke="currentColor" strokeWidth={sw} strokeLinecap="round" />
        </>
      )}
      {kind === "void" && (
        <circle cx="12" cy="12" r="8" stroke="currentColor" strokeWidth={sw} strokeDasharray="3 3" />
      )}
      {kind === "fail" && (
        <>
          <circle cx="12" cy="12" r="8" stroke="currentColor" strokeWidth={sw} />
          <path d="M9 9l6 6M15 9l-6 6" stroke="currentColor" strokeWidth={sw} strokeLinecap="round" />
        </>
      )}
      {kind === "bridge" && (
        <path d="M4 16V8M20 16V8M4 12h16M8 16v-3M12 16v-3M16 16v-3" stroke="currentColor" strokeWidth={sw} />
      )}
      {kind === "signal" && (
        <>
          <circle cx="12" cy="16" r="1.5" fill="currentColor" />
          <path d="M7 12a5 5 0 0110 0M5 9a7 7 0 0114 0" stroke="currentColor" strokeWidth={sw} strokeLinecap="round" />
        </>
      )}
      {kind === "atelier" && (
        <>
          <rect x="5" y="6" width="14" height="12" rx="2" stroke="currentColor" strokeWidth={sw} />
          <path d="M5 10h14" stroke="currentColor" strokeWidth={sw} />
        </>
      )}
    </svg>
  );
}

function postJson(url: string, body: unknown) {
  return fetch(url, {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify(body),
  });
}

function ModeSwitch({ current }: { current: string }) {
  const [busy, setBusy] = useState(false);
  return (
    <div className={`flex rounded-full border ${INK.line} p-0.5`}>
      {MODES.map((gear) => (
        <button
          key={gear}
          type="button"
          disabled={busy}
          onClick={() => {
            setBusy(true);
            void postJson("/api/mode", { mode: gear }).finally(() => setBusy(false));
          }}
          className={`rounded-full px-3 py-1 text-[11px] uppercase tracking-wider ${
            current === gear ? "bg-[#7aa2ff] text-[#0b0e14]" : `${INK.mute} hover:text-[#e8edf7]`
          }`}
        >
          {gear}
        </button>
      ))}
    </div>
  );
}

function TaskList({ tasks, empty }: { tasks: ControlTask[]; empty: string }) {
  if (!tasks.length) {
    return (
      <p className={`flex items-center gap-2 text-sm italic ${INK.dim}`}>
        <Icon kind="void" />
        {empty}
      </p>
    );
  }
  return (
    <ul className="space-y-2">
      {tasks.map((t) => (
        <li key={t.id} className={`rounded-lg border ${INK.line} px-3 py-2`}>
          <div className="flex items-baseline justify-between gap-2">
            <p className="text-sm font-medium">
              {t.id} · {t.title}
            </p>
            <span className={`text-[11px] uppercase tracking-wider ${INK.mute}`}>
              {t.status}
            </span>
          </div>
          <p className={`mt-1 text-[11px] ${INK.dim}`}>
            {t.lane} · {t.owner}
            {t.next_action ? ` · ${t.next_action}` : ""}
          </p>
        </li>
      ))}
    </ul>
  );
}

function RunGrid({ runs }: { runs: AgentRun[] }) {
  if (!runs.length) {
    return (
      <p className={`flex items-center gap-2 text-sm italic ${INK.dim}`}>
        <Icon kind="void" />
        No check-ins
      </p>
    );
  }
  return (
    <div className="grid gap-3 md:grid-cols-2">
      {runs.map((run) => (
        <article key={run.id} className={`rounded-lg border ${INK.line} px-3 py-3`}>
          <div className="flex items-center justify-between gap-2">
            <h3 className="flex items-center gap-2 font-semibold tracking-wide uppercase">
              <Icon kind={run.status === "failed" ? "fail" : run.status === "done" ? "check" : "pulse"} />
              {run.agent_id}
            </h3>
            <span className={`text-[11px] uppercase tracking-wider ${INK.mute}`}>{run.status}</span>
          </div>
          <p className={`mt-1 text-xs uppercase tracking-wider ${INK.accent}`}>
            {run.phase} {run.task_id ? `· ${run.task_id}` : ""}
          </p>
          <p className="mt-2 text-sm">{run.mission || "—"}</p>
        </article>
      ))}
    </div>
  );
}

function LiveFallback({ agents }: { agents: LiveAgent[] }) {
  if (!agents.length) {
    return null;
  }
  return (
    <p className={`mt-2 text-[11px] ${INK.dim}`}>
      Live files: {agents.map((a) => `${a.id} (${a.freshness})`).join(" · ")}
    </p>
  );
}

function ServiceBoard({ items, note }: { items: ServiceItem[]; note?: string }) {
  const [busy, setBusy] = useState<string | null>(null);
  if (!items.length) {
    return <p className={`text-sm italic ${INK.dim}`}>{note || "Nothing registered — greenfield."}</p>;
  }
  return (
    <ul className="space-y-2">
      {items.map((svc) => (
        <li key={svc.name} className={`flex items-center justify-between gap-3 rounded-lg border ${INK.line} px-3 py-2`}>
          <div>
            <p className="text-sm font-medium">{svc.name}</p>
            <p className={`text-[11px] uppercase tracking-wider ${INK.mute}`}>{svc.status}</p>
          </div>
          <div className="flex gap-2">
            {(["up", "down"] as const).map((action) => (
              <button
                key={action}
                type="button"
                disabled={busy === svc.name}
                onClick={() => {
                  setBusy(svc.name);
                  void postJson(`/api/services/${svc.name}`, { action }).finally(() => setBusy(null));
                }}
                className={`rounded-md border ${INK.line} px-2 py-1 text-[11px] uppercase tracking-wider ${INK.mute} hover:text-[#e8edf7]`}
              >
                {action}
              </button>
            ))}
          </div>
        </li>
      ))}
    </ul>
  );
}

function CreateTask() {
  const [title, setTitle] = useState("");
  const [busy, setBusy] = useState(false);
  return (
    <form
      className="mt-3 flex gap-2"
      onSubmit={(e) => {
        e.preventDefault();
        if (!title.trim()) return;
        setBusy(true);
        void postJson("/api/tasks", { title: title.trim(), lane: "now", status: "queued" })
          .then(() => setTitle(""))
          .finally(() => setBusy(false));
      }}
    >
      <input
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        placeholder="New task title"
        className={`min-w-0 flex-1 rounded-md border ${INK.line} bg-[#0b0e14] px-3 py-2 text-sm outline-none`}
      />
      <button
        type="submit"
        disabled={busy}
        className="rounded-md bg-[#7aa2ff] px-3 py-2 text-[11px] font-semibold uppercase tracking-wider text-[#0b0e14]"
      >
        Create
      </button>
    </form>
  );
}

function WaitHero({ task }: { task: ControlTask }) {
  const [busy, setBusy] = useState(false);
  const act = (path: string) => {
    setBusy(true);
    void fetch(path, { method: "POST" }).finally(() => setBusy(false));
  };
  return (
    <section className={`${INK.panel} border-[#f5a524]/40 p-5 lg:col-span-3`}>
      <p className={`mb-2 flex items-center gap-2 text-[11px] uppercase tracking-[0.16em] ${INK.wait}`}>
        <Icon kind="wait" />
        WAITING_FOR_USER
      </p>
      <h2 className="text-lg font-semibold">
        {task.id} · {task.title}
      </h2>
      <p className={`mt-2 text-sm ${INK.mute}`}>{task.next_action || "A decision is required. Jarvis will not guess."}</p>
      <div className="mt-4 flex flex-wrap gap-2">
        <button
          type="button"
          disabled={busy}
          onClick={() => act(`/api/tasks/${task.id}/resume`)}
          className="rounded-md bg-[#7aa2ff] px-3 py-2 text-[11px] font-semibold uppercase tracking-wider text-[#0b0e14]"
        >
          Resume
        </button>
        <button
          type="button"
          disabled={busy}
          onClick={() => act(`/api/tasks/${task.id}/not-now`)}
          className={`rounded-md border ${INK.line} px-3 py-2 text-[11px] uppercase tracking-wider ${INK.mute}`}
        >
          Not now
        </button>
      </div>
    </section>
  );
}

function OccasionChrome({ occasion }: { occasion: string }) {
  const map: Record<string, { icon: Mark; label: string }> = {
    deep: { icon: "bridge", label: "Deep work" },
    away: { icon: "signal", label: "Away glance" },
    showcase: { icon: "atelier", label: "Showcase" },
    crisis: { icon: "wait", label: "Crisis wait" },
  };
  const row = map[occasion] || map.away;
  return (
    <span className={`flex items-center gap-1.5 rounded-full bg-[#121722] px-2 py-0.5 uppercase tracking-wider ${INK.mute}`}>
      <Icon kind={row.icon} className="h-3.5 w-3.5" />
      {row.label}
    </span>
  );
}

export function App() {
  const state = useCockpit();
  if (!state) {
    return <main className={`p-8 ${INK.mute}`}>Connecting to workroom…</main>;
  }
  const health = state.kit_health.status;
  const watching = state.watching ?? 0;
  const occasion = state.occasion || "away";
  const tasks = state.tasks ?? [];
  const runs = state.runs ?? [];
  const waiting = state.waiting;
  const nowTasks = tasks.filter((t) => t.lane === "now");
  const dense = occasion === "deep";
  const showcase = occasion === "showcase";

  return (
    <div className="min-h-screen">
      <header className={`flex flex-wrap items-center justify-between gap-3 border-b ${INK.line} px-6 py-4`}>
        <h1 className="text-lg font-semibold uppercase tracking-[0.16em]">Mission Control</h1>
        <div className={`flex flex-wrap items-center gap-3 text-xs ${INK.mute}`}>
          <OccasionChrome occasion={occasion} />
          <span
            className={`flex items-center gap-1.5 rounded-full px-2 py-0.5 uppercase tracking-wider ${
              watching > 0 ? "bg-[#143325] text-[#3dd68c]" : "bg-[#121722] text-[#6b7385]"
            }`}
          >
            <Icon kind="eye" className="h-3.5 w-3.5" />
            {watching > 0 ? `Watching · ${watching}` : "Not watching"}
          </span>
          <ModeSwitch current={state.mode || "unknown"} />
          <span
            className={`rounded-full px-2 py-0.5 uppercase tracking-wider ${
              health === "STALE" ? "bg-[#3a2a10] text-[#f5a524]" : "bg-[#143325] text-[#3dd68c]"
            }`}
          >
            {health}
          </span>
        </div>
      </header>
      <main className={`grid gap-4 p-6 ${dense ? "lg:grid-cols-2" : "lg:grid-cols-3"}`}>
        {waiting ? <WaitHero task={waiting} /> : null}
        {occasion === "away" && !waiting ? (
          <section className={`${INK.panel} p-5 lg:col-span-3`}>
            <p className={`mb-2 flex items-center gap-2 text-[11px] uppercase tracking-[0.16em] ${INK.accent}`}>
              <Icon kind="signal" />
              Active
            </p>
            <p className="text-lg font-semibold">{state.mission || "No mission line yet"}</p>
            <p className={`mt-2 text-sm ${INK.mute}`}>{state.next_task || "Nothing waiting."}</p>
            <CreateTask />
          </section>
        ) : null}
        {showcase || dense || occasion === "crisis" ? (
          <section className={`${INK.panel} p-4 ${dense ? "" : "lg:col-span-1"}`}>
            <h2 className={`mb-2 flex items-center gap-2 text-[11px] uppercase tracking-[0.16em] ${INK.accent}`}>
              Mission
            </h2>
            <p className={showcase ? "text-xl font-semibold" : "text-sm"}>{state.mission || "—"}</p>
            <h2 className={`mb-2 mt-4 text-[11px] uppercase tracking-[0.16em] ${INK.accent}`}>Next</h2>
            <p className="text-sm">{state.next_task || "—"}</p>
            <CreateTask />
          </section>
        ) : null}
        <section className={`${INK.panel} p-4 ${occasion === "away" ? "lg:col-span-2" : ""}`}>
          <h2 className={`mb-3 flex items-center gap-2 text-[11px] uppercase tracking-[0.16em] ${INK.accent}`}>
            <Icon kind="pulse" />
            NOW
          </h2>
          <TaskList tasks={nowTasks} empty="empty" />
        </section>
        <section className={`${INK.panel} p-4 ${dense || occasion === "crisis" ? "lg:col-span-2" : "lg:col-span-3"}`}>
          <h2 className={`mb-3 flex items-center gap-2 text-[11px] uppercase tracking-[0.16em] ${INK.accent}`}>
            Agent runs
          </h2>
          <RunGrid runs={runs} />
          <LiveFallback agents={state.live} />
        </section>
        <section className={`${INK.panel} p-4`}>
          <h2 className={`mb-2 text-[11px] uppercase tracking-[0.16em] ${INK.accent}`}>HAPPY · services</h2>
          <ServiceBoard items={state.service_board?.items ?? []} note={state.service_board?.note} />
        </section>
      </main>
    </div>
  );
}
