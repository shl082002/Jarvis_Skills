"""Store + tracker sync tests. Run from api/: python3 -m pytest test_store.py -q"""
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from dispatch import deploy_run, explain_run, stop_run, write_principal_reply
from store import create_task, derive_occasion, list_tasks, update_task, upsert_run
from tracker_sync import export_tracker, import_tracker_if_empty


class StoreTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.wr = Path(self.tmp.name)

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_task_survives_reconnect(self) -> None:
        created = create_task(self.wr, title="Prove face", lane="now", status="queued")
        self.assertTrue(created["id"].startswith("T-"))
        again = list_tasks(self.wr)
        self.assertEqual(len(again), 1)
        self.assertEqual(again[0]["title"], "Prove face")

    def test_waiting_and_not_now(self) -> None:
        t = create_task(self.wr, title="Need ruling")
        update_task(self.wr, t["id"], status="waiting_for_user", lane="awaiting")
        tasks = list_tasks(self.wr)
        self.assertEqual(derive_occasion(tasks, []), "crisis")
        parked = update_task(self.wr, t["id"], status="parked", lane="parked")
        self.assertEqual(parked["lane"], "parked")
        self.assertEqual(derive_occasion(list_tasks(self.wr), []), "away")
        create_task(self.wr, title="Idle now", lane="now", status="queued")
        self.assertEqual(derive_occasion(list_tasks(self.wr), []), "away")

    def test_run_makes_deep(self) -> None:
        t = create_task(self.wr, title="Build", lane="now", status="running")
        upsert_run(self.wr, run_id="friday", agent_id="friday", task_id=t["id"], status="running")
        self.assertEqual(derive_occasion(list_tasks(self.wr), [{"status": "running"}]), "deep")

    def test_import_export_tracker(self) -> None:
        (self.wr / "TRACKER.md").write_text(
            "# TRACKER — next free ID: T-3\n\n"
            "## NOW — being worked\n"
            "- **T-2** · Seeded item · owner: assistant · next: demo\n\n"
            "## AWAITING — blocked\n*(none)*\n\n"
            "## NEXT — open, queued\n*(none)*\n\n"
            "## PARKED — deferred\n*(none)*\n\n"
            "## DONE — recent\n*(none)*\n",
            encoding="utf-8",
        )
        n = import_tracker_if_empty(self.wr)
        self.assertEqual(n, 1)
        self.assertEqual(import_tracker_if_empty(self.wr), 0)
        export_tracker(self.wr)
        text = (self.wr / "TRACKER.md").read_text(encoding="utf-8")
        self.assertIn("**T-2**", text)
        self.assertIn("Seeded item", text)

    def test_deploy_stop_explain(self) -> None:
        (self.wr / "MODE.md").write_text("mode: build\n", encoding="utf-8")
        t = create_task(self.wr, title="Wire verbs", lane="now")
        out = deploy_run(self.wr, task_id=t["id"], agent_id="dum-e")
        self.assertEqual(out["run"]["status"], "queued")
        self.assertEqual(out["dispatch"]["action"], "deploy")
        explained = explain_run(self.wr, out["run"]["id"])
        self.assertIn("dum-e", explained["summary"])
        stopped = stop_run(self.wr, out["run"]["id"])
        self.assertEqual(stopped["run"]["status"], "stopped")
        self.assertEqual(stopped["dispatch"]["action"], "stop")

    def test_discuss_blocks_friday(self) -> None:
        (self.wr / "MODE.md").write_text("mode: discuss\n", encoding="utf-8")
        t = create_task(self.wr, title="No mutate")
        with self.assertRaises(ValueError):
            deploy_run(self.wr, task_id=t["id"], agent_id="friday")
        deploy_run(self.wr, task_id=t["id"], agent_id="dum-e")

    def test_principal_reply_inbox(self) -> None:
        t = create_task(self.wr, title="Gym question")
        inbox = write_principal_reply(self.wr, task_id=t["id"], text="use port 3847")
        self.assertEqual(inbox["action"], "reply")
        self.assertFalse(inbox["parked"])
        on_disk = (self.wr / "dispatch.json").read_text(encoding="utf-8")
        self.assertIn("use port 3847", on_disk)
        self.assertIn("\"action\": \"reply\"", on_disk)


if __name__ == "__main__":
    unittest.main()
