import { useEffect, useState } from "react";
import type { CockpitState } from "./types";

function wsUrl(): string {
  const proto = window.location.protocol === "https:" ? "wss" : "ws";
  return `${proto}://${window.location.host}/api/stream`;
}

export function useCockpit(): CockpitState | null {
  const [state, setState] = useState<CockpitState | null>(null);

  useEffect(() => {
    let cancelled = false;
    const pull = () => {
      void fetch("/api/state")
        .then((r) => r.json())
        .then((next: CockpitState) => {
          if (!cancelled) {
            setState(next);
          }
        })
        .catch(() => undefined);
    };
    pull();
    const socket = new WebSocket(wsUrl());
    socket.onmessage = (event) => {
      try {
        const next = JSON.parse(event.data) as CockpitState;
        if (!cancelled) {
          setState(next);
        }
      } catch {
        /* ignore bad frames */
      }
    };
    window.addEventListener("jarvis-refresh", pull);
    const poll = window.setInterval(pull, 4000);
    return () => {
      cancelled = true;
      socket.close();
      window.removeEventListener("jarvis-refresh", pull);
      window.clearInterval(poll);
    };
  }, []);

  return state;
}
