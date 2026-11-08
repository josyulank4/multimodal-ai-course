"""Media cost model: cost per resolved outcome (Lesson 34)."""
CASES, RESOLVED = 10000, 8200
IMAGE_COST, VLM_COST = 0.004, 0.021
AUTO_SHARE, VLM_SHARE = 0.70, 0.30


def price(cases, image_cost, vlm_cost, vlm_share):
    auto_share = 1.0 - vlm_share
    return cases * (auto_share * image_cost + vlm_share * vlm_cost)


def report(label, total, resolved):
    print(f"{label}: ${total:.2f} a month, ${total / resolved:.4f} per resolved outcome")


def levers():
    cascade = price(CASES, IMAGE_COST, VLM_COST, 0.15)
    report("lever 1 - cascade, vlm share 0.30 to 0.15", cascade, RESOLVED)
    resized = price(CASES, 0.002, VLM_COST, 0.15)
    report("lever 2 - resize, image cost 0.004 to 0.002", resized, RESOLVED)
    print(f"perceived queue: 6000 of {CASES} cases")
    perceived = price(6000, 0.002, VLM_COST, 0.15)
    report("lever 3 - perceive less, last here, first in life", perceived, RESOLVED)


def sensitivity():
    report("sensitivity - resolved halves to 4100", price(CASES, IMAGE_COST, VLM_COST, VLM_SHARE), RESOLVED // 2)
    report("sensitivity - vlm share creeps to 0.60", price(CASES, IMAGE_COST, VLM_COST, 0.60), RESOLVED)


def main():
    total = price(CASES, IMAGE_COST, VLM_COST, VLM_SHARE)
    print(f"queue: {CASES} cases, {RESOLVED} resolved")
    print(f"monthly media cost: ${total:.2f}")
    print(f"cost per resolved outcome: ${total / RESOLVED:.4f}")
    levers()
    sensitivity()
    print("mediacost demo complete")


if __name__ == "__main__": main()
