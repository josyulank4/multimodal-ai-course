"""Capstone: the parcel system — fused decision + storm sizing (Lessons 46, 51)."""

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


# LESSON 51 START SCAFFOLD: the capstone as lesson 46 left it, plus an
# inline review sketch in main. The finished lesson replaces the sketch
# with CASES, evidence, fuse, and review functions above main.

def main():
    verdict()
    sizing(PEAK_PER_HOUR, PER_STAGE_S)
    headroom(PEAK_PER_HOUR)
    degrade()
    storm_night()

    cases = [
        ("crushed corner, books", 86),
        ("waterlogged paperbacks", 45),
        ("claims the box arrived empty", 240),
    ]
    for name, value in cases:
        print(f"review sketch: {name} (${value}) — evidence not yet fused")
    print("verdict: SHIP — gate passed, cost model closed, rollout staged")
    print("parcelcapstone demo complete")


if __name__ == "__main__":
    main()
