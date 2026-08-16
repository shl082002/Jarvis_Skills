type Kind =
  | "eye"
  | "pulse"
  | "wait"
  | "check"
  | "void"
  | "fail"
  | "bridge"
  | "signal"
  | "atelier"
  | "bolt";

export function Mark({
  kind,
  className = "h-[1.1rem] w-[1.1rem]",
}: {
  kind: Kind;
  className?: string;
}) {
  const sw = 1.6;
  return (
    <svg className={className} viewBox="0 0 24 24" fill="none" aria-hidden>
      {kind === "eye" && (
        <>
          <ellipse cx="12" cy="12" rx="8" ry="5" stroke="currentColor" strokeWidth={sw} />
          <circle cx="12" cy="12" r="2.2" fill="currentColor" />
        </>
      )}
      {kind === "bolt" && (
        <path
          d="M13 2L4 14h7l-1 8 10-14h-7l1-6z"
          stroke="currentColor"
          strokeWidth={sw}
          strokeLinejoin="round"
        />
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
