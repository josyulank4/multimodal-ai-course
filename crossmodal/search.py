"""Cross-modal retrieval over a tiny shared embedding space (Lesson 22)."""
import math

# One tiny shared space, three dimensions, every number visible.
# Each photo and each text query is a vector in the SAME space; the
# components are (garment-red, garment-blue/denim, damage/context).
CATALOG = [
    ("photo:red-jacket-front", (0.90, 0.10, 0.20)),
    ("photo:red-jacket-back", (0.84, 0.22, 0.18)),
    ("photo:blue-jeans", (0.10, 0.90, 0.15)),
    ("photo:parcel-damage", (0.20, 0.15, 0.95)),
    ("photo:warehouse-aisle", (0.30, 0.30, 0.40)),
    ("photo:red-cap", (0.78, 0.30, 0.28)),
]
# Withdrawn by its owner: it must never be returned, whatever it scores.
WITHDRAWN = {"photo:red-cap"}
QUERIES = {
    "red jacket": (0.85, 0.12, 0.25),
    "damaged parcel": (0.25, 0.20, 0.90),
}


def cosine(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(y * y for y in b))
    return dot / (na * nb)


def rank(query, items=CATALOG):
    visible = [(name, vec) for name, vec in items if name not in WITHDRAWN]
    return sorted(visible, key=lambda kv: cosine(query, kv[1]), reverse=True)


def main():
    for label, query in QUERIES.items():
        print(f'query: "{label}" {query}')
        for name, vec in rank(query):
            print(f"  {name}: cosine {cosine(query, vec):.3f}")
        print(f"top hit: {rank(query)[0][0]}")
    print("crossmodal demo complete")


if __name__ == "__main__":
    main()
