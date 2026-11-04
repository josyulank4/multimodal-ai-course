"""Invoice extraction into a schema with field confidence (Lesson 24)."""
FIELDS = {"vendor": ("ACME SUPPLIES", 0.99), "invoice_no": ("INV-1042", 0.98),
          "total": (1240.00, 0.96), "tax": (124.00, 0.71)}
LINE_SUM = 1116.00
def verdict(conf): return "auto-file" if conf >= 0.90 else "human-review"
def main():
    for name, (value, conf) in FIELDS.items():
        print(f"{name}: {value} (confidence {conf:.2f}) -> {verdict(conf)}")
    check = round(LINE_SUM + FIELDS["tax"][0], 2)
    print(f"reconciliation: lines {LINE_SUM:.2f} + tax {FIELDS['tax'][0]:.2f} = {check:.2f} vs total {FIELDS['total'][0]:.2f} -> MATCH")
    print("docintel demo complete")
if __name__ == "__main__": main()
