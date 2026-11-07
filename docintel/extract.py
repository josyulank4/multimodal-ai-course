"""Invoice extraction into a schema with field confidence (Lesson 18)."""
import re

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

FIELD_CONFIDENCE = {"vendor": 0.99, "invoice_no": 0.98,
                    "lines": 0.97, "tax": 0.71, "total": 0.96}
AUTO_FILE_AT = 0.90


def verdict(conf):
    return "auto-file" if conf >= AUTO_FILE_AT else "human-review"


def money(token):
    return float(token)


def parse(text):
    fields = {}
    lines = []
    for raw in text.splitlines():
        line = raw.strip()
        m = re.match(r"(.+?)\s+(\d+)\s+(\d+(?:\.\d{2})?)\s+(\d+(?:\.\d{2})?)", line)
        if m:
            qty, unit, ext = int(m.group(2)), money(m.group(3)), money(m.group(4))
            ok = abs(round(qty * unit, 2) - ext) < 0.005
            lines.append((m.group(1), qty, unit, ext, ok))
            continue
        low = line.lower()
        if low.startswith("tax invoice") or " - " in line:
            fields["vendor"] = line.split(" - ")[0].strip()
        elif low.startswith("invoice no:"):
            fields["invoice_no"] = line.split(":", 1)[1].strip()
        elif low.startswith("subtotal:"):
            fields["subtotal"] = money(line.rsplit(" ", 1)[1])
        elif low.startswith("tax"):
            fields["tax"] = money(line.rsplit(" ", 1)[1])
        elif low.startswith("total due:"):
            fields["total"] = money(line.rsplit(" ", 1)[1])
    fields["lines"] = lines
    return fields


def main():
    f = parse(INVOICE_TEXT)
    print("field verdicts (schema: value, confidence, route):")
    print(f"vendor: {f['vendor']} (confidence {FIELD_CONFIDENCE['vendor']:.2f}) -> {verdict(FIELD_CONFIDENCE['vendor'])}")
    print(f"invoice_no: {f['invoice_no']} (confidence {FIELD_CONFIDENCE['invoice_no']:.2f}) -> {verdict(FIELD_CONFIDENCE['invoice_no'])}")
    print(f"line items: {len(f['lines'])} parsed from text")
    for name, qty, unit, ext, ok in f["lines"]:
        print(f"  line: {name} {qty} x {unit:.2f} = {ext:.2f} -> arithmetic {'OK' if ok else 'FAIL'}")
    lines_ok = all(l[4] for l in f["lines"])
    line_sum = round(sum(l[3] for l in f["lines"]), 2)
    print(f"lines: {line_sum:.2f} (confidence {FIELD_CONFIDENCE['lines']:.2f}) -> {verdict(FIELD_CONFIDENCE['lines'])}")
    print(f"tax: {f['tax']:.2f} (confidence {FIELD_CONFIDENCE['tax']:.2f}) -> {verdict(FIELD_CONFIDENCE['tax'])}")
    print(f"total: {f['total']:.2f} (confidence {FIELD_CONFIDENCE['total']:.2f}) -> {verdict(FIELD_CONFIDENCE['total'])}")
    check = round(line_sum + f["tax"], 2)
    state = "MATCH" if check == f["total"] and lines_ok else "MISMATCH"
    print(f"reconciliation: lines {line_sum:.2f} + tax {f['tax']:.2f} = {check:.2f} vs total {f['total']:.2f} -> {state}")
    if state == "MATCH":
        print("document route: auto-file (tax field flagged human-review)")
    else:
        print("document route: human-review (reconciliation failed)")
    print("docintel demo complete")


if __name__ == "__main__":
    main()
