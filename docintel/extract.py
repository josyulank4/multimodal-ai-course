"""Invoice extraction into a schema with field confidence (Lesson 18)."""
# START SCAFFOLD - the invoice is the input; the extractor is the lesson.
INVOICE_TEXT = """ACME SUPPLIES - TAX INVOICE
invoice no: INV-1042
billed to: Northwind Traders

description            qty   unit      extension
widget housings        4     120.00    480.00
sensor brackets        6     45.50     273.00
calibration service    1     263.00    263.00
platform support hours 2     50        100

subtotal: 1116.00
tax (10%): 124.00
total due: 1240.00"""

# TODO (lesson 18): parse the invoice text into the schema, attach a
# confidence to every field, check every line's arithmetic
# (qty x unit == extension), reconcile lines + tax against the total,
# and route the document: auto-file or human-review.
