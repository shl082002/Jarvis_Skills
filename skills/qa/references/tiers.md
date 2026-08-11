# QA tiers

**Critical** — cannot complete a primary path; data loss; auth bypass; money
wrong; uncaught crash on the happy path.

**High** — primary path works only with a workaround; wrong state shown as
success; cannot recover without refresh/restart.

**Medium** — secondary path broken; confusing but completable; missing
validation that does not corrupt data.

**Cosmetic** — spacing, copy tone, unused empty state, visual nits. Exhaustive
only unless the principal filed it as a feel defect (charter: product feel is
a spec).

Quick = critical + high. Standard adds medium. Exhaustive adds cosmetic.
Stop when the tier is covered — do not binge the rest “while you’re there.”
