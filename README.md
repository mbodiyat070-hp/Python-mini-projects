# Python Mini-Projects

A collection of small Python programs I've built while learning the language,
organised by topic. Each one is short, self-contained, and runnable with just
Python (standard library only) so I can keep practising the fundamentals.

## Projects

| Folder | Program | What it practises |
|--------|---------|-------------------|
| `01_fundamentals` | `temperature_converter.py` | Functions, arithmetic, validated user input |
| `02_data_structures` | `word_frequency.py` | Dictionaries, loops, string handling |
| `03_algorithms` | `binary_search.py` | Searching a sorted list efficiently |
| `04_files_and_data` | `csv_summary.py` | Reading a CSV, validating rows, summarising data |
| `05_oop` | `bank_account.py` | Classes, methods, input validation |
| `06_games` | `trivia_game.py` | A quiz game with scoring and randomness |

## Running any project

```bash
cd 01_fundamentals
python temperature_converter.py
```

Each file has a short comment at the top explaining what it does and how to
run it. The `csv_summary` project reads the included `sales.csv`, which
deliberately contains three bad rows (non-numeric quantity, negative values,
missing category) so you can see the validation reject them.

## Skills demonstrated

- **Data validation** — every program that takes input defends itself:
  the converter re-asks on non-numeric input instead of crashing, the CSV
  summary skips and reports malformed rows instead of corrupting totals,
  the bank account rejects invalid amounts, and the trivia game normalises
  answers before comparing
- **Core Python** — functions, type hints, dictionaries, tuples,
  `try`/`except`, f-strings, the `csv` and `pathlib` modules
- **Object-oriented programming** — a class with methods that protect its
  own state (`05_oop`)
- **Algorithms** — binary search with a clear loop invariant (`03_algorithms`)
- **Readable code** — docstrings, small single-purpose functions, and
  consistent naming across all six programs

## What I learned

- Crashing on bad input is a bug, not the user's fault — a loop with
  `try`/`except ValueError` turns a crash into a re-prompt
- When processing a data file, skipping and *reporting* bad rows is far more
  useful than either crashing or silently ignoring them — you can see exactly
  what was wrong and where (the same idea I used in my
  [nova-data-engine](https://github.com/mbodiyat070-hp/nova-data-engine)
  pipeline)
- Splitting programs into small functions makes them testable — validation
  logic that lives in its own function can be checked without running the
  whole program

## What I'm working on next

- Adding a few small tests for the functions
- A project that reads data from a public API
- Reworking the CSV summary to write its results back out to a new file
