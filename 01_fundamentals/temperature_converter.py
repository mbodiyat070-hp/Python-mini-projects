"""
Temperature converter — practises functions, arithmetic and input.

Converts between Celsius and Fahrenheit.
Run:  python temperature_converter.py
"""


def celsius_to_fahrenheit(celsius: float) -> float:
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5 / 9


def main() -> None:
    print("1) Celsius to Fahrenheit")
    print("2) Fahrenheit to Celsius")
    choice = input("Choose 1 or 2: ").strip()

    if choice == "1":
        c = float(input("Temperature in Celsius: "))
        print(f"{c}°C = {celsius_to_fahrenheit(c):.1f}°F")
    elif choice == "2":
        f = float(input("Temperature in Fahrenheit: "))
        print(f"{f}°F = {fahrenheit_to_celsius(f):.1f}°C")
    else:
        print("Please choose 1 or 2.")


if __name__ == "__main__":
    main()
