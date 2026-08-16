export const INK = {
  mute: "text-[#8b95a8]",
  dim: "text-[#6b7385]",
  line: "border-[#243044]",
  panel: "rounded-[0.75rem] border border-[#243044] bg-[#121722]",
  accent: "text-[#7aa2ff]",
  ok: "text-[#3dd68c]",
  wait: "text-[#f5a524]",
};

export const OCCASION_RAIL: Record<string, string> = {
  deep: "bg-[#7aa2ff]",
  crisis: "bg-[#f5a524]",
  showcase: "bg-[#3dd68c]",
  away: "bg-[#6b7385]",
};

export const MIX: Record<string, string> = {
  deep: "Command 70% · Atelier 20% · Signal 10%",
  away: "Signal 75% · Atelier 15% · Command 10%",
  showcase: "Atelier 70% · Signal 20% · Command 10%",
  crisis: "Signal hero + Command strip",
};

export const OCCASION_COPY: Record<
  string,
  { title: string; emotion: string; need: string; mark: "bolt" | "signal" | "atelier" | "wait" }
> = {
  deep: {
    title: "Deep work",
    emotion: "Vigilance + agency",
    need: "See everything that moves; act without hunting.",
    mark: "bolt",
  },
  away: {
    title: "Away glance",
    emotion: "Calm trust",
    need: "One breath: am I needed?",
    mark: "signal",
  },
  showcase: {
    title: "Showcase / leave open",
    emotion: "Quiet pride",
    need: "The room should feel competent — not noisy.",
    mark: "atelier",
  },
  crisis: {
    title: "Crisis wait",
    emotion: "Tension held kindly",
    need: "Stop is unmistakable; next action is one click away.",
    mark: "wait",
  },
};
