import type { LiveAgent } from "./types";
import { useCockpit } from "./useCockpit";

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

export function App() {
  const state = useCockpit();
  if (!state) {
    return (
      <main className="p-8 text-[#8b95a8]">Connecting to workroom…</main>
    );
  }
  const health = state.kit_health.status;
  return (
    <div className="min-h-screen">
      <header className="flex items-baseline justify-between border-b border-[#243044] px-6 py-4">
        <h1 className="text-lg font-semibold uppercase tracking-[0.16em]">
          Heimdall
        </h1>
        <div className="text-xs text-[#8b95a8]">
          <span
            className={`mr-3 rounded-full px-2 py-0.5 uppercase tracking-wider ${
              health === "STALE"
                ? "bg-[#3a2a10] text-[#f5a524]"
                : "bg-[#143325] text-[#3dd68c]"
            }`}
          >
            {health}
          </span>
          {state.generated_at}
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
            AWAITING
          </h2>
          <List items={state.lanes.awaiting} empty="none" />
        </section>
      </main>
    </div>
  );
}
