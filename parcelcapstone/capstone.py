"""Capstone: the parcel system — fused decision + storm sizing (Lesson 51)."""

PEAK_PER_HOUR = 4200
PER_STAGE_S = 1.8
SHED_ORDER = (
    "pause the nightly replay batch",
    "sample routine re-checks to one in three",
    "route ambiguous cases to the human queue, verdicts later",
    "never shed: capture, provenance, the safety filter",
)


def verdict():
    print("capstone: photo damaged 0.82 + form denied + voice damaged -> gate ESCALATE then human confirms damage")
    print("decision: refund issued with full evidence trail")


def workers_needed(peak, per_stage_s):
    return int(-(-peak * per_stage_s // 3600))


def sizing(peak, per_stage_s):
    print(f"storm sizing: {peak} cases/hour needs {workers_needed(peak, per_stage_s)} parallel workers at {per_stage_s}s per case")


def headroom(peak):
    workers = workers_needed(PEAK_PER_HOUR, PER_STAGE_S)
    capacity = int(workers * 3600 / PER_STAGE_S)
    print(f"headroom: {workers} workers clear {capacity} cases/hour — {(capacity - peak) / peak:.0%} above the {peak} forecast peak")


def degrade():
    print("degradation order, decided in advance, in writing:")
    for i, step in enumerate(SHED_ORDER, 1):
        print(f"  {i}. {step}")
    print("the order is the policy; the storm does not get a vote")


def storm_night():
    print("the night the queue ate the peak: 9000 arrived, forecast 4200")
    sizing(9000, PER_STAGE_S)
    print("the queue absorbed two hours; shed steps 1-2 fired in order; the urgent lane never waited")
    print("oldest urgent case at midnight: 4 minutes — inside the promise")


CASES = (
    ("crushed corner, books", 0.82, "clear", "matches", 86),
    ("waterlogged paperbacks", 0.77, "denied", "matches", 45),
    ("claims the box arrived empty", 0.12, "denied", "insists damage", 240),
)
REVIEW_VALUE_LIMIT = 200


def evidence(case):
    name, photo, form, voice, value = case
    print(f"evidence: {name} — photo damage {photo:.2f}, form {form}, voice {voice}, claim ${value}")


def fuse(case):
    name, photo, form, voice, value = case
    if value > REVIEW_VALUE_LIMIT:
        return "ESCALATE — value above $200 buys a human decision"
    if photo >= 0.70 and form == "clear" and voice == "matches":
        return "APPROVE — senses agree, damage confirmed"
    if photo < 0.30 and form == "denied":
        return "ESCALATE — senses conflict: photo clear, form denied, voice insists"
    return "ESCALATE — human confirms the fused evidence"


def review():
    print("capstone review: three cases, fused evidence, one standard")
    approved = escalated = 0
    for case in CASES:
        evidence(case)
        outcome = fuse(case)
        print(f"review: {case[0]} -> {outcome}")
        if outcome.startswith("APPROVE"):
            approved += 1
        else:
            escalated += 1
    print(f"review outcome: {approved} approved on evidence, {escalated} escalated to humans")
    print("review gate: whole-system gate PASS — agreement and slices inside thresholds")
    print("review cost: closed at $0.0111 per resolved case, first month inside the band")
    print("review rollout: shadow complete, canary senses live, widening on evidence")
    print("blockers: none — every escalation above is the design working, not failing")


def main():
    verdict()
    sizing(PEAK_PER_HOUR, PER_STAGE_S)
    headroom(PEAK_PER_HOUR)
    degrade()
    storm_night()
    review()
    print("verdict: SHIP — gate passed, cost model closed, rollout staged")
    print("parcelcapstone demo complete")


if __name__ == "__main__":
    main()
