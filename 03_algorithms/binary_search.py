"""
Binary search — practises algorithms and lists.

Finds the position of a target value in a sorted list by repeatedly halving
the search range. Much faster than checking every item.
Run:  python binary_search.py
"""


def binary_search(values: list[int], target: int) -> int:
    """Return the index of target in a sorted list, or -1 if not found."""
    low, high = 0, len(values) - 1
    while low <= high:
        mid = (low + high) // 2
        if values[mid] == target:
            return mid
        if values[mid] < target:
            low = mid + 1      # target is in the right half
        else:
            high = mid - 1     # target is in the left half
    return -1


def main() -> None:
    numbers = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    for target in (23, 72, 40):
        result = binary_search(numbers, target)
        if result == -1:
            print(f"{target} is not in the list")
        else:
            print(f"{target} found at index {result}")


if __name__ == "__main__":
    main()
