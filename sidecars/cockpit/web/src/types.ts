export type LiveAgent = {
  id: string;
  role: string;
  mission: string;
  phase: string;
  status: string;
  freshness: "fresh" | "stale" | "unknown";
  last_beat: string;
};

export type CockpitState = {
  generated_at: string;
  workroom: string;
  mission: string;
  next_task: string;
  lanes: { now: string[]; awaiting: string[]; awaiting_count: number };
  branches: string[];
  services: string;
  reports: { name: string; mtime: string | null }[];
  live: LiveAgent[];
  kit_health: {
    stale: boolean;
    status: string;
    beat_fresh_seconds: number;
  };
};
