import { useState } from "react";
import { postJson } from "../lib/api";
import { INK } from "../lib/ink";

export function CreateTask() {
  const [title, setTitle] = useState("");
  const [busy, setBusy] = useState(false);
  return (
    <form
      className="mt-[1vh] flex gap-[0.6vw]"
      onSubmit={(e) => {
        e.preventDefault();
        if (!title.trim()) return;
        setBusy(true);
        void postJson("/api/tasks", { title: title.trim(), lane: "now", status: "queued" })
          .then(() => setTitle(""))
          .finally(() => setBusy(false));
      }}
    >
      <input
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        placeholder="New task title"
        className={`min-w-0 flex-1 rounded-[0.4rem] border ${INK.line} bg-[#0b0e14] px-[0.9vw] py-[1vh] text-[0.9rem] outline-none`}
      />
      <button
        type="submit"
        disabled={busy}
        className="rounded-[0.4rem] bg-[#7aa2ff] px-[1vw] py-[1vh] text-[0.65rem] font-semibold uppercase tracking-wider text-[#0b0e14]"
      >
        Create
      </button>
    </form>
  );
}
