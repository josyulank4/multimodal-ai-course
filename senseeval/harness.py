"""Multimodal evaluation harness: per-slice scores + release gate (Lesson 44)."""
SLICES = {"vision-clear": (48, 50), "vision-lowlight": (31, 50), "voice-clean": (46, 50), "voice-noisy": (38, 50)}
FLOOR = 0.80
def main():
    blocked = []
    for name, (ok, n) in SLICES.items():
        rate = ok / n; print(f"{name}: {ok}/{n} = {rate:.2f}")
        if rate < FLOOR: blocked.append(name)
    print(f"gate: FAIL — slices below floor {FLOOR}: {', '.join(blocked)}" if blocked else "gate: PASS")
    print("senseeval demo complete")
if __name__ == "__main__": main()
