"""Fusion gate: weighted evidence + disagreement escalation (Lesson 26)."""
EVIDENCE = {"photo": ("damaged", 0.82), "form": ("denied", 0.64), "voice": ("damaged", 0.77)}
WEIGHTS = {"photo": 0.45, "form": 0.25, "voice": 0.30}
# START SCAFFOLD (Lesson 26): the evidence and the weights are
# data — three senses, one claim, one dissent already visible.
# The lesson writes, on screen: REASON (why each sense voted as
# it did), score_claim() (validation first: unknown, missing and
# out-of-range senses refused by name; then the weighted loop
# with one AUDIT line per vote), decide() (the gate: disagreement
# outranks score) and main() (the shipped output, plus the trail).
# TODO(student): implement score_claim, decide and main so the
# shipped claim scores 0.600 yet still escalates, and every vote
# leaves a signed line in the audit trail.
