"""Fusion gate: weighted evidence + disagreement escalation (Lesson 32)."""
EVIDENCE = {"photo": ("damaged", 0.82), "form": ("denied", 0.64), "voice": ("damaged", 0.77)}
WEIGHTS = {"photo": 0.45, "form": 0.25, "voice": 0.30}
def main():
    score = 0.0
    for sense, (claim, conf) in EVIDENCE.items():
        vote = 1.0 if claim == "damaged" else 0.0
        score += WEIGHTS[sense] * vote * conf
        print(f"{sense}: claims {claim} (confidence {conf:.2f}, weight {WEIGHTS[sense]})")
    verdicts = {c for c, _ in EVIDENCE.values()}
    print(f"fusion score: {score:.3f}")
    print("gate: ESCALATE — senses disagree" if len(verdicts) > 1 else "gate: DECIDE")
    print("fusiongate demo complete")
if __name__ == "__main__": main()
