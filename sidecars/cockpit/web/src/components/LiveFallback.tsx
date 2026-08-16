import { HiOutlineRadio } from "react-icons/hi2";
import { INK } from "../lib/ink";
import type { LiveAgent } from "../types";

export function LiveFallback({ agents }: { agents: LiveAgent[] }) {
  if (!agents.length) {
    return <p className={`text-[0.9rem] italic ${INK.dim}`}>No live beats — quiet house.</p>;
  }
  return (
    <div className="grid gap-[1vh] md:grid-cols-2">
      {agents.map((agent) => (
        <article key={agent.id} className={`rounded-[0.5rem] border ${INK.line} px-[0.9vw] py-[1.2vh]`}>
          <div className="flex items-center justify-between gap-[0.8vw]">
            <h3 className="flex items-center gap-[0.5vw] font-semibold tracking-wide uppercase">
              <HiOutlineRadio className="h-[1.1rem] w-[1.1rem]" />
              {agent.id}
            </h3>
            <span className={`text-[0.65rem] uppercase tracking-wider ${INK.mute}`}>{agent.status}</span>
          </div>
          <p className={`mt-[0.4vh] text-[0.7rem] uppercase tracking-wider ${INK.accent}`}>{agent.phase}</p>
          <p className="mt-[0.8vh] text-[0.9rem]">{agent.mission || "—"}</p>
        </article>
      ))}
    </div>
  );
}
