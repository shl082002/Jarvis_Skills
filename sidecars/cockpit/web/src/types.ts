export type LiveAgent = {
  id: string;
  role: string;
  mission: string;
  phase: string;
  status: string;
  freshness: "fresh" | "stale" | "unknown";
  last_beat: string;
};

export type ServiceItem = {
  name: string;
  status: string;
  detail: string;
};

export type ControlTask = {
  id: string;
  title: string;
  lane: string;
  status: string;
  owner: string;
  next_action: string;
  created_at: string;
  updated_at: string;
};

export type AgentRun = {
  id: string;
  task_id: string | null;
  agent_id: string;
  role: string;
  mission: string;
  phase: string;
  status: string;
  report_path: string;
  started_at: string;
  last_beat_at: string;
  ended_at: string | null;
};

export type CockpitState = {
  generated_at: string;
  workroom: string;
  mission: string;
  next_task: string;
  mode: string;
  watching: number;
  occasion?: "deep" | "away" | "showcase" | "crisis";
  waiting?: ControlTask | null;
  tasks?: ControlTask[];
  runs?: AgentRun[];
  lanes: { now: string[]; awaiting: string[]; awaiting_count: number };
  branches: string[];
  services: string;
  service_board: { items: ServiceItem[]; note?: string };
  reports: { name: string; mtime: string | null }[];
  live: LiveAgent[];
  fleet?: string[];
  dispatch?: {
    action: string;
    run_id: string;
    task_id?: string;
    agent_id: string;
    mission?: string;
    hands?: string;
    at?: string;
  } | null;
  kit_health: {
    stale: boolean;
    status: string;
    beat_fresh_seconds: number;
  };
  gauntlet?: { on: boolean; reason: string };
};
