"""
CSV summary — practises reading files and the csv module.

Reads a small sales CSV and reports total revenue per category. This is a
tiny version of the data-handling a data engineer does: read raw data,
group it, and summarise it.
Run:  python csv_summary.py
"""

import csv
from pathlib import Path

CSV_PATH = Path(__file__).parent / "sales.csv"


def revenue_by_category(path: Path) -> dict[str, float]:
    totals: dict[str, float] = {}
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            category = row["category"]
            revenue = int(row["quantity"]) * float(row["price"])
            totals[category] = totals.get(category, 0.0) + revenue
    return totals


def main() -> None:
    totals = revenue_by_category(CSV_PATH)
    print("Revenue by category:")
    for category, total in sorted(totals.items()):
        print(f"  {category}: £{total:.2f}")
    print(f"  TOTAL: £{sum(totals.values()):.2f}")


if __name__ == "__main__":
    main()
