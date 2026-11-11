"""
Ohm's Law and Power Calculator
CTE123 Python Mini Project
"""

import math


def get_number(prompt):
    """Ask for a valid, non-negative number."""
    while True:
        try:
            value = float(input(prompt))
            if not math.isfinite(value):
                print("Please enter a finite number.")
            elif value < 0:
                print("Please enter zero or a positive number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number, such as 12 or 3.5.")


def calculate(target, first, second, value1, value2):
    """Calculate the requested quantity from two known quantities."""
    values = {first: value1, second: value2}

    if target == "voltage":
        if first == "current" and second == "resistance":
            return value1 * value2
        elif first == "power" and second == "current":
            if value2 == 0:
                raise ZeroDivisionError
            return value1 / value2
        else:  # Power and resistance
            return math.sqrt(value1 * value2)

    elif target == "current":
        if first == "voltage" and second == "resistance":
            if value2 == 0:
                raise ZeroDivisionError
            return value1 / value2
        elif first == "power" and second == "voltage":
            if value2 == 0:
                raise ZeroDivisionError
            return value1 / value2
        else:  # Power and resistance
            if value2 == 0:
                raise ZeroDivisionError
            return math.sqrt(value1 / value2)

    elif target == "resistance":
        if first == "voltage" and second == "current":
            if value2 == 0:
                raise ZeroDivisionError
            return value1 / value2
        elif first == "voltage" and second == "power":
            if value2 == 0:
                raise ZeroDivisionError
            return (value1 ** 2) / value2
        else:  # Power and current
            if value2 == 0:
                raise ZeroDivisionError
            return value1 / (value2 ** 2)

    else:  # Power
        if first == "voltage" and second == "current":
            return value1 * value2
        elif first == "voltage" and second == "resistance":
            if value2 == 0:
                raise ZeroDivisionError
            return (value1 ** 2) / value2
        else:  # Current and resistance
            return (value1 ** 2) * value2


def main():
    """Run the calculator until the user chooses to quit."""
    units = {
        "voltage": "V",
        "current": "A",
        "resistance": "ohms",
        "power": "W"
    }

    # Each target has three valid pairs of known quantities.
    choices = {
        "1": ("voltage", [("current", "resistance"),
                          ("power", "current"),
                          ("power", "resistance")]),
        "2": ("current", [("voltage", "resistance"),
                          ("power", "voltage"),
                          ("power", "resistance")]),
        "3": ("resistance", [("voltage", "current"),
                             ("voltage", "power"),
                             ("power", "current")]),
        "4": ("power", [("voltage", "current"),
                        ("voltage", "resistance"),
                        ("current", "resistance")])
    }

    history = []

    while True:
        print("\n===== OHM'S LAW AND POWER CALCULATOR =====")
        print("1. Calculate voltage (V)")
        print("2. Calculate current (I)")
        print("3. Calculate resistance (R)")
        print("4. Calculate power (P)")
        print("5. View calculation history")
        print("6. Quit")

        selection = input("Choose an option (1-6): ").strip()

        if selection == "6":
            print("Thank you for using the calculator. Goodbye!")
            break

        elif selection == "5":
            if not history:
                print("No calculations have been made yet.")
            else:
                print("\n--- Calculation History ---")
                for number, record in enumerate(history, start=1):
                    print(f"{number}. {record}")
        elif selection in choices:
            target, pairs = choices[selection]

            print(f"\nTo calculate {target}, choose the two values you know:")
            for index, pair in enumerate(pairs, start=1):
                print(f"{index}. {pair[0].title()} and {pair[1].title()}")

            pair_choice = input("Choose a pair (1-3): ").strip()

            if pair_choice in ("1", "2", "3"):
                first, second = pairs[int(pair_choice) - 1]
                value1 = get_number(f"Enter {first} ({units[first]}): ")
                value2 = get_number(f"Enter {second} ({units[second]}): ")

                try:
                    answer = calculate(target, first, second, value1, value2)
                    if not math.isfinite(answer):
                        print("The result is too large to calculate.")
                        continue

                    result = f"{target.title()} = {answer:.4f} {units[target]}"
                    print("\nResult:", result)
                    history.append(result)
                except ZeroDivisionError:
                    print("Cannot divide by zero. Please try another set of values.")
            else:
                print("Invalid pair choice. Please choose 1, 2 or 3.")
        else:
            print("Invalid menu option. Please choose a number from 1 to 6.")


if __name__ == "__main__":
    main()
