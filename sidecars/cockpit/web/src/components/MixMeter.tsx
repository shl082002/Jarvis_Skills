export type MixSegment = { label: string; pct: number; fill: string };

export function mixSegments(occasion: string): MixSegment[] {
  if (occasion === "deep") {
    return [
      { label: "Command", pct: 70, fill: "#7aa2ff" },
      { label: "Atelier", pct: 20, fill: "#3d4a63" },
      { label: "Signal", pct: 10, fill: "#243044" },
    ];
  }
  if (occasion === "away") {
    return [
      { label: "Signal", pct: 75, fill: "#7aa2ff" },
      { label: "Atelier", pct: 15, fill: "#3d4a63" },
      { label: "Command", pct: 10, fill: "#243044" },
    ];
  }
  if (occasion === "showcase") {
    return [
      { label: "Atelier", pct: 70, fill: "#3dd68c" },
      { label: "Signal", pct: 20, fill: "#3d4a63" },
      { label: "Command", pct: 10, fill: "#243044" },
    ];
  }
  return [
    { label: "Signal hero", pct: 55, fill: "#f5a524" },
    { label: "Command strip", pct: 35, fill: "#3d4a63" },
    { label: "Atelier calm", pct: 10, fill: "#243044" },
  ];
}

export function MixMeter({ occasion }: { occasion: string }) {
  const segments = mixSegments(occasion);
  return (
    <div>
      <div className="flex h-[1vh] min-h-[8px] overflow-hidden rounded-[0.3rem]">
        {segments.map((s) => (
          <div
            key={s.label}
            className="h-full"
            style={{ width: `${s.pct}%`, background: s.fill }}
            title={`${s.label} ${s.pct}%`}
          />
        ))}
      </div>
      <div className="mt-[0.8vh] flex flex-wrap gap-[1.2vw] text-[0.65rem] uppercase tracking-wider text-[#8b95a8]">
        {segments.map((s) => (
          <span key={s.label}>
            {s.label} {s.pct}%
          </span>
        ))}
      </div>
    </div>
  );
}
