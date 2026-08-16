import { useState } from "react";
import { HiOutlineMinusCircle } from "react-icons/hi2";
import { postJson } from "../lib/api";
import { INK } from "../lib/ink";
import type { ControlTask } from "../types";

export function TaskRow({
  task,
  fleet,
  mode,
}: {
  task: ControlTask;
  fleet: string[];
  mode: string;
}) {
  const options = fleet.length ? fleet : ["dum-e"];
  const [agent, setAgent] = useState(options[0]);
  const [busy, setBusy] = useState(false);
  const [err, setErr] = useState("");
  const canDeploy =
    (task.lane === "now" || task.lane === "next") &&
    (task.status === "queued" || task.status === "running" || task.status === "verifying");
  return (
    <li className={`rounded-[0.5rem] border ${INK.line} px-[0.9vw] py-[1vh]`}>
      <div className="flex items-baseline justify-between gap-[0.8vw]">
        <p className="text-[0.9rem] font-medium">
          {task.id} · {task.title}
        </p>
        <span className={`text-[0.65rem] uppercase tracking-wider ${INK.mute}`}>{task.status}</span>
      </div>
      <p className={`mt-[0.4vh] text-[0.65rem] ${INK.dim}`}>
        {task.lane} · {task.owner}
        {task.next_action ? ` · ${task.next_action}` : ""}
      </p>
      {err ? <p className={`mt-[0.4vh] text-[0.65rem] ${INK.wait}`}>{err}</p> : null}
      {canDeploy ? (
      <div className="mt-[0.8vh] flex flex-wrap items-center gap-[0.6vw]">
        <select
          value={agent}
          onChange={(e) => setAgent(e.target.value)}
          className={`rounded-[0.35rem] border ${INK.line} bg-[#0b0e14] px-[0.6vw] py-[0.4vh] text-[0.65rem] uppercase tracking-wider`}
        >
          {options.map((id) => (
            <option key={id} value={id}>
              {id}
            </option>
          ))}
        </select>
        <button
          type="button"
          disabled={busy}
          onClick={() => {
            setBusy(true);
            setErr("");
            void postJson("/api/runs/deploy", { task_id: task.id, agent_id: agent })
              .catch((e: Error) => setErr(e.message))
              .finally(() => setBusy(false));
          }}
          className="rounded-[0.35rem] bg-[#7aa2ff] px-[0.8vw] py-[0.4vh] text-[0.65rem] font-semibold uppercase tracking-wider text-[#0b0e14]"
        >
          Deploy
        </button>
        {mode === "discuss" || mode === "plan" ? (
          <span className={`text-[0.6rem] ${INK.dim}`}>FRIDAY blocked until build</span>
        ) : null}
      </div>
      ) : null}
    </li>
  );
}

export function TaskList({
  tasks,
  empty,
  fleet,
  mode,
}: {
  tasks: ControlTask[];
  empty: string;
  fleet: string[];
  mode: string;
}) {
  if (!tasks.length) {
    return (
      <p className={`flex items-center gap-[0.5vw] text-[0.9rem] italic ${INK.dim}`}>
        <HiOutlineMinusCircle className="h-[1.1rem] w-[1.1rem]" />
        {empty}
      </p>
    );
  }
  return (
    <ul className="space-y-[0.8vh]">
      {tasks.map((t) => (
        <TaskRow key={t.id} task={t} fleet={fleet} mode={mode} />
      ))}
    </ul>
  );
}
