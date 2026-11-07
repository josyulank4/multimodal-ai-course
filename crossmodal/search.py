"""Cross-modal retrieval over a tiny shared embedding space (Lesson 22)."""
import math

# One tiny shared space, three dimensions, every number visible.
# Catalog photos are embedded by the CURRENT image encoder; text
# queries are embedded by the text encoder. Both claim the component
# order (red garment, blue garment, hard surface) — a claim worth
# checking, because the previous image encoder release shipped its
# first two components swapped, and its vectors are still on disk.
CATALOG = [
    ("photo:red-jacket-front", "encoder-v2", (0.90, 0.10, 0.20)),
    ("photo:red-jacket-back", "encoder-v2", (0.84, 0.22, 0.18)),
    ("photo:blue-jeans", "encoder-v1", (0.88, 0.12, 0.15)),
    ("photo:parcel-damage", "encoder-v2", (0.20, 0.15, 0.95)),
    ("photo:warehouse-aisle", "encoder-v2", (0.30, 0.30, 0.40)),
    ("photo:red-cap", "encoder-v2", (0.78, 0.30, 0.28)),
]
# encoder-v1 wrote (blue garment, red garment, hard surface): the
# first two components are swapped against the space's contract.
LEGACY_ENCODERS = {"encoder-v1"}
# Withdrawn by its owner: it must never be returned, whatever it scores.
WITHDRAWN = {"photo:red-cap"}
QUERIES = {
    "red jacket": (0.85, 0.12, 0.25),
    "damaged parcel": (0.25, 0.20, 0.90),
}


def repaired(name, encoder, vec):
    """A legacy vector, repaired into the space's component order."""
    if encoder in LEGACY_ENCODERS:
        return (vec[1], vec[0], vec[2])
    return vec


def cosine(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(y * y for y in b))
    return dot / (na * nb)


def rank(query, items=CATALOG):
    visible = [(name, repaired(name, enc, vec))
               for name, enc, vec in items if name not in WITHDRAWN]
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
