"""Capstone: the parcel system — fused decision + storm sizing (Lesson 46)."""

PEAK_PER_HOUR = 4200
PER_STAGE_S = 1.8

# START SCAFFOLD: the shipped inline demo (Lesson 46 builds the functions live).
# The finished lesson replaces everything below this marker.
def main():
    print("capstone: photo damaged 0.82 + form denied + voice damaged -> gate ESCALATE then human confirms damage")
    print("decision: refund issued with full evidence trail")
    peak, per_stage_s = 4200, 1.8
    workers = int(-(-peak * per_stage_s // 3600))
    print(f"storm sizing: {peak} cases/hour needs {workers} parallel workers at {per_stage_s}s per case")
    print("verdict: SHIP — gate passed, cost model closed, rollout staged")
    print("parcelcapstone demo complete")
if __name__ == "__main__": main()
