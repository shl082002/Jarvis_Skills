import { ServiceBoard } from "../components/ServiceBoard";
import { INK } from "../lib/ink";
import type { CockpitState } from "../types";

export function ServicesPage({ state }: { state: CockpitState }) {
  return (
    <div className="mx-auto max-w-[96rem] pb-[4vh]">
      <section className={`${INK.panel} p-[1.6vw]`}>
        <p className={`mb-[1.2vh] text-[0.65rem] uppercase tracking-[0.16em] ${INK.accent}`}>Services</p>
        <ServiceBoard items={state.service_board.items} note={state.service_board.note} />
      </section>
    </div>
  );
}
