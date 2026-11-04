"""Media cost model: cost per resolved outcome (Lesson 40)."""
def main():
    cases, resolved = 10000, 8200
    image_cost, vlm_cost = 0.004, 0.021
    auto_share, vlm_share = 0.70, 0.30
    total = cases * (auto_share * image_cost + vlm_share * vlm_cost)
    print(f"queue: {cases} cases, {resolved} resolved")
    print(f"monthly media cost: ${total:.2f}")
    print(f"cost per resolved outcome: ${total/resolved:.4f}")
    print("mediacost demo complete")
if __name__ == "__main__": main()
