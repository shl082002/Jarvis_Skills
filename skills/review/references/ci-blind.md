# Bugs that pass CI

Walk every item. Skip only with a written reason.

- **Wrong success:** UI or API reports OK while the ledger/store disagrees
- **Idempotency:** retry duplicates a side effect (orders, mints, mails)
- **Authz gap:** tests hit the happy role; another role can mutate
- **Race / time:** assumes single-threaded or local clock
- **Event vs poll:** client will miss a state change the server already made
- **Silent swallow:** catch-all, empty except, ignored webhook failures
- **PII / secrets:** tokens, emails, or `.env` values in logs or new files
- **Flag default:** new path on for everyone, or dark path that can never enable
- **Migration one-way:** no rollback story; backfill assumed
- **Test theater:** assertion too weak; mocks the unit under test
- **Cross-boundary lie:** frontend relabels an ugly enum the API still emits
- **Delete / cancel:** money or seats not released; orphan rows

Money, identity, and audit paths get a second pass even if the rest is clean.
