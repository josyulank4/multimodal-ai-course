"""Multimodal evaluation harness: per-slice scores + release gate (Lesson 38)."""
import math

SLICES = [("vision-clear", 48, 50, "vision team"),
          ("vision-lowlight", 31, 50, "capture team"),
          ("voice-clean", 46, 50, "speech team"),
          ("voice-noisy", 38, 50, "speech team")]
FLOOR = 0.80


def rate(ok, n):
    return ok / n


def shortfall(ok, n):
    return math.ceil(FLOOR * n) - ok


def report():
    for name, ok, n, owner in SLICES:
        r = rate(ok, n)
        margin = r - FLOOR
        if r < FLOOR:
            state = f"{shortfall(ok, n)} short of the floor"
        else:
            state = "holds"
        print(f"{name}: {ok}/{n} = {r:.2f} (margin {margin:+.2f}, {state})")


def gate_line(blocked):
    if blocked:
        return f"gate: FAIL — slices below floor {FLOOR}: {', '.join(blocked)}"
    return "gate: PASS"


def gate():
    blocked = []
    for name, ok, n, owner in SLICES:
        if rate(ok, n) < FLOOR:
            blocked.append(name)
    print(gate_line(blocked))
    owners = {name: owner for name, ok, n, owner in SLICES}
    for name in blocked:
        print(f"owner: {name} -> {owners[name]}")
    return blocked


def budget():
    costs = [("golden run", 14.40), ("judge audit", 6.25), ("human spot-check", 9.60)]
    total = sum(c for _, c in costs)
    cases = sum(n for _, _, n, _ in SLICES)
    for label, c in costs:
        print(f"cost - {label}: ${c:.2f} ({c / total * 100:.1f}% of the gate)")
    print(f"evaluation budget: ${total:.2f} for {cases} cases, ${total / cases:.4f} per case")


def flip():
    name, ok, n, owner = SLICES[3]
    need = shortfall(ok, n)
    print(f"flip drill - {name}: {need} more passing cases reach the floor: "
          f"{ok + need}/{n} = {rate(ok + need, n):.2f}")
    print("flip drill - gate still FAIL: vision-lowlight remains below the floor")
    print("one slice repaired is not a release")


def main():
    ok_all = sum(ok for _, ok, n, _ in SLICES)
    n_all = sum(n for _, _, n, _ in SLICES)
    print(f"blended: {ok_all}/{n_all} = {rate(ok_all, n_all):.2f} - "
          "above the floor, and not the number that decides")
    report()
    gate()
    budget()
    flip()
    print("senseeval demo complete")


if __name__ == "__main__":
    main()
