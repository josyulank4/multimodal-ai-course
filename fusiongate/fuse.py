"""Fusion gate: weighted evidence + disagreement escalation (Lesson 26)."""
EVIDENCE = {"photo": ("damaged", 0.82), "form": ("denied", 0.64), "voice": ("damaged", 0.77)}
WEIGHTS = {"photo": 0.45, "form": 0.25, "voice": 0.30}
REASON = {
    "photo": "bumper crease + paint transfer in frame",
    "form": "claimant ticked 'no damage' at intake",
    "voice": "driver describes the impact on the recording",
}
THRESHOLD = 0.5
AUDIT = []


def audit_trail():
    """The signed lines this junction leaves behind, oldest first."""
    return list(AUDIT)


def score_claim(evidence=None, weights=None):
    """Weighted support for 'damaged', with every vote audited.

    Raises ValueError naming the sense on unknown or missing senses
    and on confidences outside [0, 1] — a junction that cannot trust
    its inputs must refuse, not average."""
    evidence = EVIDENCE if evidence is None else evidence
    weights = WEIGHTS if weights is None else weights
    for sense in evidence:
        if sense not in weights:
            raise ValueError(f"unknown sense: {sense}")
    for sense in weights:
        if sense not in evidence:
            raise ValueError(f"missing sense: {sense}")
    score = 0.0
    verdicts = set()
    for sense, (claim, conf) in evidence.items():
        if not 0.0 <= conf <= 1.0:
            raise ValueError(f"confidence out of range: {sense} {conf}")
        vote = 1.0 if claim == "damaged" else 0.0
        part = weights[sense] * vote * conf
        score += part
        verdicts.add(claim)
        AUDIT.append(f"{sense}: {claim} @{conf:.2f} x{weights[sense]:.2f} "
                     f"-> +{part:.3f} ({REASON.get(sense, 'no reason recorded')})")
    return score, verdicts


def decide(evidence=None, weights=None):
    """The gate: disagreement outranks score, always."""
    score, verdicts = score_claim(evidence, weights)
    if len(verdicts) > 1:
        return "ESCALATE", score
    return ("DECIDE-DAMAGED" if score >= THRESHOLD else "DECIDE-NOT-DAMAGED"), score


def main():
    for sense, (claim, conf) in EVIDENCE.items():
        print(f"{sense}: claims {claim} (confidence {conf:.2f}, weight {WEIGHTS[sense]})")
    gate, score = decide()
    print(f"fusion score: {score:.3f}")
    print("gate: ESCALATE — senses disagree" if gate == "ESCALATE"
          else f"gate: DECIDE ({gate})")
    print("audit trail:")
    for line in audit_trail():
        print(f"  {line}")
    print("fusiongate demo complete")


if __name__ == "__main__":
    main()
