"""Media cost model: cost per resolved outcome (Lesson 34)."""
CASES, RESOLVED = 10000, 8200
IMAGE_COST, VLM_COST = 0.004, 0.021
AUTO_SHARE, VLM_SHARE = 0.70, 0.30
# START SCAFFOLD: the shipped demo prices one queue inline in main().
# This lesson grows it into functions: price() holds the arithmetic,
# report() prints one honest line per scenario, levers() applies the
# savings in order, sensitivity() names the assumption that
# bankrupts the model if it is wrong.
def main():
    total = CASES * (AUTO_SHARE * IMAGE_COST + VLM_SHARE * VLM_COST)
    print(f"queue: {CASES} cases, {RESOLVED} resolved")
    print(f"monthly media cost: ${total:.2f}")
    print(f"cost per resolved outcome: ${total / RESOLVED:.4f}")
    print("mediacost demo complete")
if __name__ == "__main__": main()
