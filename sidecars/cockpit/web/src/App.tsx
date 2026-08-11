import { useState } from "react";
import type { LiveAgent, ServiceItem } from "./types";
import { useCockpit } from "./useCockpit";

const MODES = ["discuss", "plan", "build"] as const;

function List({ items, empty }: { items: string[]; empty: string }) {
  if (!items.length) {
    return <p className="text-sm italic text-[#6b7385]">{empty}</p>;
  }
  return (
    <ul className="list-disc space-y-1 pl-5 text-sm">
      {items.map((item) => (
        <li key={item}>{item}</li>
      ))}
    </ul>
  );
}

function freshnessClass(agent: LiveAgent): string {
  if (agent.freshness === "fresh") {
    return "border-[#3dd68c]/40 bg-[#143325]";
  }
  if (agent.freshness === "stale") {
    return "border-[#f5a524]/30 bg-[#3a2a10]";
  }
  return "border-[#243044] bg-[#0b0e14]";
}

function LivePanel({ agents }: { agents: LiveAgent[] }) {
  if (!agents.length) {
    return <p className="text-sm italic text-[#6b7385]">No check-ins</p>;
  }
  return (
    <div className="grid gap-3 md:grid-cols-2">
      {agents.map((agent) => (
        <article
          key={agent.id}
          className={`rounded-lg border px-3 py-3 ${freshnessClass(agent)}`}
        >
          <div className="flex items-baseline justify-between gap-2">
            <h3 className="font-semibold tracking-wide uppercase">{agent.id}</h3>
            <span className="text-[11px] uppercase tracking-wider text-[#8b95a8]">
              {agent.freshness} · {agent.status}
            </span>
          </div>
          <p className="mt-1 text-xs uppercase tracking-wider text-[#7aa2ff]">
            {agent.phase || "—"} {agent.role ? `· ${agent.role}` : ""}
          </p>
          <p className="mt-2 text-sm">{agent.mission || "—"}</p>
        </article>
      ))}
    </div>
  );
}

function ModeSwitch({ current }: { current: string }) {
  const [busy, setBusy] = useState(false);
  return (
    <div className="flex rounded-full border border-[#243044] p-0.5">
      {MODES.map((gear) => (
        <button
          key={gear}
          type="button"
          disabled={busy}
          onClick={() => {
            setBusy(true);
            void fetch("/api/mode", {
              method: "POST",
              headers: { "content-type": "application/json" },
              body: JSON.stringify({ mode: gear }),
            }).finally(() => setBusy(false));
          }}
          className={`rounded-full px-3 py-1 text-[11px] uppercase tracking-wider ${
            current === gear
              ? "bg-[#7aa2ff] text-[#0b0e14]"
              : "text-[#8b95a8] hover:text-[#e8edf7]"
          }`}
        >
          {gear}
        </button>
      ))}
    </div>
  );
}

function ServiceBoard({
  items,
  note,
}: {
  items: ServiceItem[];
  note?: string;
}) {
  const [busy, setBusy] = useState<string | null>(null);
  if (!items.length) {
    return (
      <p className="text-sm italic text-[#6b7385]">
        {note || "Nothing registered — greenfield."}
      </p>
    );
  }
  return (
    <ul className="space-y-2">
      {items.map((svc) => (
        <li
          key={svc.name}
          className="flex items-center justify-between gap-3 rounded-lg border border-[#243044] px-3 py-2"
        >
          <div>
            <p className="text-sm font-medium">{svc.name}</p>
            <p className="text-[11px] uppercase tracking-wider text-[#8b95a8]">
              {svc.status}
            </p>
          </div>
          <div className="flex gap-2">
            {(["up", "down"] as const).map((action) => (
              <button
                key={action}
                type="button"
                disabled={busy === svc.name}
                onClick={() => {
                  setBusy(svc.name);
                  void fetch(`/api/services/${svc.name}`, {
                    method: "POST",
                    headers: { "content-type": "application/json" },
                    body: JSON.stringify({ action }),
                  }).finally(() => setBusy(null));
                }}
                className="rounded-md border border-[#243044] px-2 py-1 text-[11px] uppercase tracking-wider text-[#8b95a8] hover:text-[#e8edf7]"
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

export function App() {
  const state = useCockpit();
  if (!state) {
    return (
      <main className="p-8 text-[#8b95a8]">Connecting to workroom…</main>
    );
  }
  const health = state.kit_health.status;
  const watching = state.watching ?? 0;
  return (
    <div className="min-h-screen">
      <header className="flex flex-wrap items-center justify-between gap-3 border-b border-[#243044] px-6 py-4">
        <h1 className="text-lg font-semibold uppercase tracking-[0.16em]">
          Heimdall
        </h1>
        <div className="flex flex-wrap items-center gap-3 text-xs text-[#8b95a8]">
          <span
            className={`rounded-full px-2 py-0.5 uppercase tracking-wider ${
              watching > 0
                ? "bg-[#143325] text-[#3dd68c]"
                : "bg-[#121722] text-[#6b7385]"
            }`}
          >
            {watching > 0 ? `Watching · ${watching}` : "Not watching"}
          </span>
          <ModeSwitch current={state.mode || "unknown"} />
          <span
            className={`rounded-full px-2 py-0.5 uppercase tracking-wider ${
              health === "STALE"
                ? "bg-[#3a2a10] text-[#f5a524]"
                : "bg-[#143325] text-[#3dd68c]"
            }`}
          >
            {health}
          </span>
        </div>
      </header>
      <main className="grid gap-4 p-6 lg:grid-cols-3">
        <section className="rounded-xl border border-[#243044] bg-[#121722] p-4 lg:col-span-3">
          <h2 className="mb-3 text-[11px] uppercase tracking-[0.16em] text-[#7aa2ff]">
            Live
          </h2>
          <LivePanel agents={state.live} />
        </section>
        <section className="rounded-xl border border-[#243044] bg-[#121722] p-4">
          <h2 className="mb-2 text-[11px] uppercase tracking-[0.16em] text-[#7aa2ff]">
            Mission
          </h2>
          <p className="text-sm">{state.mission || "—"}</p>
          <h2 className="mb-2 mt-4 text-[11px] uppercase tracking-[0.16em] text-[#7aa2ff]">
            Next
          </h2>
          <p className="text-sm">{state.next_task || "—"}</p>
        </section>
        <section className="rounded-xl border border-[#243044] bg-[#121722] p-4">
          <h2 className="mb-2 text-[11px] uppercase tracking-[0.16em] text-[#7aa2ff]">
            NOW
          </h2>
          <List items={state.lanes.now} empty="empty" />
        </section>
        <section className="rounded-xl border border-[#243044] bg-[#121722] p-4">
          <h2 className="mb-2 text-[11px] uppercase tracking-[0.16em] text-[#7aa2ff]">
            HAPPY · services
          </h2>
          <ServiceBoard
            items={state.service_board?.items ?? []}
            note={state.service_board?.note}
          />
        </section>
      </main>
    </div>
  );
}
