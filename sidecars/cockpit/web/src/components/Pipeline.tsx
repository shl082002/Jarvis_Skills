import { INK } from "../lib/ink";

const STAGES = ["Plan", "Run", "Wait", "Done"] as const;

export function Pipeline({
  mode,
  running,
  waiting,
}: {
  mode: string;
  running: number;
  waiting: boolean;
}) {
  let active: (typeof STAGES)[number] = "Plan";
  if (waiting) active = "Wait";
  else if (running > 0) active = "Run";
  else if (mode === "build") active = "Run";
  else if (mode === "plan") active = "Plan";

  return (
    <div className="flex flex-wrap items-center gap-[0.8vw]">
      {STAGES.map((name, i) => (
        <span key={name} className="flex items-center gap-[0.8vw]">
          <span
            className={`rounded-[0.4rem] border px-[0.9vw] py-[0.6vh] text-[0.7rem] uppercase tracking-wider ${
              active === name
                ? "border-[#7aa2ff] text-[#7aa2ff]"
                : `border-[#243044] ${INK.dim}`
            }`}
          >
            {name}
          </span>
          {i < STAGES.length - 1 ? <span className={INK.dim}>→</span> : null}
        </span>
      ))}
    </div>
  );
}
