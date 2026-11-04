"""Perceive-ground-act-verify agent loop with a step budget (Lesson 36)."""
SCREEN = {"refund_button": (0.72, 0.88), "approve_button": (0.25, 0.88)}
def main():
    steps = 0; budget = 5
    for action in ["perceive: claim screen captured", "ground: refund_button at (0.72, 0.88)", "act: click refund_button", "verify: status changed to refund-issued"]:
        steps += 1; print(f"step {steps}: {action}")
    print(f"agent finished in {steps} steps of {budget} budget — outcome verified")
    print("lookagent demo complete")
if __name__ == "__main__": main()
