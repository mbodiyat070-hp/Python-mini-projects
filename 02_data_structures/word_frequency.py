"""
Word frequency counter — practises dictionaries, loops and strings.

Counts how many times each word appears in a piece of text and prints
the most common ones.
Run:  python word_frequency.py
"""


def count_words(text: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for word in text.lower().split():
        word = word.strip(".,!?;:'\"")   # remove basic punctuation
        if word:
            counts[word] = counts.get(word, 0) + 1
    return counts


def top_words(counts: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    # sort by count, highest first, and take the top n
    return sorted(counts.items(), key=lambda pair: pair[1], reverse=True)[:n]


def main() -> None:
    sample = (
        "the quick brown fox jumps over the lazy dog. "
        "the dog was not amused, but the fox was quick."
    )
    counts = count_words(sample)
    print("Most common words:")
    for word, count in top_words(counts):
        print(f"  {word}: {count}")


if __name__ == "__main__":
    main()
