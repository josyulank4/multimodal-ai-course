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
# START SCAFFOLD (Lesson 22): the catalog and the withdrawn set are
# data. The lesson writes, on screen: cosine() (the transparent
# arithmetic), rank() (withdrawn filtered first, then cosine order),
# QUERIES and main() (both ranked tables printed in full).
# TODO(student): implement cosine, rank, QUERIES and main so that
# "red jacket" retrieves photo:red-jacket-front and a withdrawn
# photo is never returned, whatever it scores.
