"""
Temperature converter — practises functions, arithmetic and input validation.

Converts between Celsius and Fahrenheit. Bad input (letters, blank, wrong
menu choice) is re-asked rather than crashing the program.
Run:  python temperature_converter.py
"""


def celsius_to_fahrenheit(celsius: float) -> float:
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5 / 9


def ask_number(prompt: str) -> float:
    """Keep asking until the user enters a valid number."""
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print(f"'{raw}' is not a number — try again (e.g. 21 or -3.5).")


def ask_choice(prompt: str, valid: set[str]) -> str:
    """Keep asking until the user enters one of the valid options."""
    while True:
        choice = input(prompt).strip()
        if choice in valid:
            return choice
        print(f"Please enter one of: {', '.join(sorted(valid))}")


def main() -> None:
    print("1) Celsius to Fahrenheit")
    print("2) Fahrenheit to Celsius")
    choice = ask_choice("Choose 1 or 2: ", {"1", "2"})

    if choice == "1":
        c = ask_number("Temperature in Celsius: ")
        print(f"{c}°C = {celsius_to_fahrenheit(c):.1f}°F")
    else:
        f = ask_number("Temperature in Fahrenheit: ")
        print(f"{f}°F = {fahrenheit_to_celsius(f):.1f}°C")


if __name__ == "__main__":
    main()
