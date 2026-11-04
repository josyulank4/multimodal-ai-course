"""Cross-modal retrieval over a tiny shared embedding space (Lesson 28)."""
import math
ITEMS = {
    "photo:red-jacket": (0.9, 0.1, 0.2), "photo:blue-jeans": (0.1, 0.9, 0.15),
    "photo:parcel-damage": (0.2, 0.15, 0.95), "photo:warehouse": (0.3, 0.3, 0.4),
}
QUERY = (0.85, 0.12, 0.25)  # text: "red jacket"
def cosine(a, b):
    dot = sum(x*y for x, y in zip(a, b)); na = math.sqrt(sum(x*x for x in a)); nb = math.sqrt(sum(y*y for y in b))
    return dot / (na * nb)
def rank(query=QUERY): return sorted(ITEMS.items(), key=lambda kv: cosine(query, kv[1]), reverse=True)
def main():
    for name, vec in rank(): print(f"{name}: cosine {cosine(QUERY, vec):.3f}")
    print(f"top hit: {rank()[0][0]}")
    print("crossmodal demo complete")
if __name__ == "__main__": main()
