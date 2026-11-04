"""Damage-triage cascade: cheap scorer first, VLM only on doubt (Lesson 16)."""
CASES = [
    ("parcel-01", 0.97, "intact"), ("parcel-02", 0.93, "intact"),
    ("parcel-03", 0.61, "crushed"), ("parcel-04", 0.55, "crushed"),
    ("parcel-05", 0.88, "intact"), ("parcel-06", 0.42, "water-damaged"),
]
def route(score):
    if score >= 0.85: return "auto-decide"
    if score >= 0.50: return "vlm-review"
    return "human-review"
def main():
    routes = {}
    for pid, score, label in CASES:
        r = route(score); routes[r] = routes.get(r, 0) + 1
        print(f"{pid}: score {score:.2f} label {label} -> {r}")
    print(f"cascade: {routes['auto-decide']}/6 auto-decided, {routes['vlm-review']} escalated to vlm, {routes['human-review']} to human")
    print("visiontriage demo complete")
if __name__ == "__main__": main()
