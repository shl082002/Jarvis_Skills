import { useState } from "react";
import { postJson } from "../lib/api";
import { INK } from "../lib/ink";
import type { ServiceItem } from "../types";

export function ServiceBoard({ items, note }: { items: ServiceItem[]; note?: string }) {
  const [busy, setBusy] = useState<string | null>(null);
  const [err, setErr] = useState("");
  if (!items.length) {
    return <p className={`text-[0.9rem] italic ${INK.dim}`}>{note || "Nothing registered — greenfield."}</p>;
  }
  return (
    <div>
      {err ? <p className={`mb-[0.8vh] text-[0.65rem] ${INK.wait}`}>{err}</p> : null}
      <ul className="space-y-[0.8vh]">
        {items.map((svc) => {
          const isBoard = svc.name === "cockpit";
          return (
            <li
              key={svc.name}
              className={`flex items-center justify-between gap-[1vw] rounded-[0.5rem] border ${INK.line} px-[0.9vw] py-[1vh]`}
            >
              <div>
                <p className="text-[0.9rem] font-medium">{svc.name}</p>
                <p className={`text-[0.65rem] uppercase tracking-wider ${INK.mute}`}>{svc.status}</p>
              </div>
              <div className="flex gap-[0.6vw]">
                <button
                  type="button"
                  disabled={busy === svc.name}
                  onClick={() => {
                    setBusy(svc.name);
                    setErr("");
                    void postJson(`/api/services/${svc.name}`, { action: "up" })
                      .catch((e: Error) => setErr(e.message))
                      .finally(() => setBusy(null));
                  }}
                  className={`rounded-[0.35rem] border ${INK.line} px-[0.8vw] py-[0.4vh] text-[0.65rem] uppercase tracking-wider ${INK.mute} hover:text-[#e8edf7]`}
                >
                  up
                </button>
                <button
                  type="button"
                  disabled={busy === svc.name || isBoard}
                  title={isBoard ? "Stopping the board from itself would kill this page" : "Stop"}
                  onClick={() => {
                    if (isBoard) return;
                    setBusy(svc.name);
                    setErr("");
                    void postJson(`/api/services/${svc.name}`, { action: "down" })
                      .catch((e: Error) => setErr(e.message))
                      .finally(() => setBusy(null));
                  }}
                  className={`rounded-[0.35rem] border ${INK.line} px-[0.8vw] py-[0.4vh] text-[0.65rem] uppercase tracking-wider ${INK.mute} hover:text-[#e8edf7] disabled:opacity-40`}
                >
                  down
                </button>
              </div>
            </li>
          );
        })}
      </ul>
    </div>
  );
}
