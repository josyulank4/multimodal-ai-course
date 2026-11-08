"""Multimodal evaluation harness: per-slice scores + release gate (Lesson 38)."""
import math

SLICES = [("vision-clear", 48, 50, "vision team"),
          ("vision-lowlight", 31, 50, "capture team"),
          ("voice-clean", 46, 50, "speech team"),
          ("voice-noisy", 38, 50, "speech team")]
FLOOR = 0.80
# START SCAFFOLD: the shipped demo scores four slices inline in main().
# This lesson grows it into functions: rate() holds the one division,
# shortfall() counts whole cases to the floor, report() prints rate,
# margin and case margin per slice, gate() keeps the shipped verdict
# line and names an owner per blocked slice, budget() prices the
# evaluation itself, flip() proves one repaired slice is not a release.
def main():
    blocked = []
    for name, ok, n, owner in SLICES:
        r = ok / n
        print(f"{name}: {ok}/{n} = {r:.2f}")
        if r < FLOOR:
            blocked.append(name)
    print(f"gate: FAIL — slices below floor {FLOOR}: {', '.join(blocked)}" if blocked else "gate: PASS")
    print("senseeval demo complete")


if __name__ == "__main__":
    main()
