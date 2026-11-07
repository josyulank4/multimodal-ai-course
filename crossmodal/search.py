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
# START SCAFFOLD (Lesson 22): the catalog, the legacy-encoder set
# and the withdrawn set are data. The lesson writes, on screen:
# repaired() (legacy vectors restored to contract order), cosine()
# (the transparent arithmetic), rank() (withdrawn filtered first,
# then cosine order), QUERIES and main() (both tables in full).
# TODO(student): implement repaired, cosine, rank, QUERIES and
# main so that "red jacket" retrieves photo:red-jacket-front, the
# legacy blue-jeans row lands last where it belongs, and a
# withdrawn photo is never returned, whatever it scores.
