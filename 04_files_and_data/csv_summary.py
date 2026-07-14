"""
CSV summary — practises reading files, the csv module and data validation.

Reads a small sales CSV and reports total revenue per category. This is a
tiny version of the data-handling a data engineer does: read raw data,
validate it, group it, and summarise it. Rows with missing fields,
non-numeric numbers or negative values are skipped and reported, not
allowed to crash the run or corrupt the totals.
Run:  python csv_summary.py
"""

import csv
from pathlib import Path

CSV_PATH = Path(__file__).parent / "sales.csv"
REQUIRED = ("category", "quantity", "price")


def validate_row(row: dict) -> tuple[dict | None, str | None]:
    """Return (clean_row, None) if the row is usable, else (None, reason)."""
    for field in REQUIRED:
        if not (row.get(field) or "").strip():
            return None, f"missing {field}"
    try:
        quantity = int(row["quantity"])
        price = float(row["price"])
    except ValueError:
        return None, "quantity/price not numeric"
    if quantity < 0 or price < 0:
        return None, "negative quantity or price"
    return {"category": row["category"].strip(),
            "revenue": quantity * price}, None


def revenue_by_category(path: Path) -> tuple[dict[str, float], list[str]]:
    totals: dict[str, float] = {}
    skipped: list[str] = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for line_number, row in enumerate(reader, start=2):  # 1 is the header
            clean, reason = validate_row(row)
            if clean is None:
                skipped.append(f"line {line_number}: {reason}")
                continue
            totals[clean["category"]] = (
                totals.get(clean["category"], 0.0) + clean["revenue"])
    return totals, skipped


def main() -> None:
    totals, skipped = revenue_by_category(CSV_PATH)
    print("Revenue by category:")
    for category, total in sorted(totals.items()):
        print(f"  {category}: £{total:.2f}")
    print(f"  TOTAL: £{sum(totals.values()):.2f}")
    if skipped:
        print(f"\nSkipped {len(skipped)} bad row(s):")
        for reason in skipped:
            print(f"  {reason}")


if __name__ == "__main__":
    main()
