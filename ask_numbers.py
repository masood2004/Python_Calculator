from ClearAndLogo import ClearAndLogo


def ask_numbers(what_function):
    while True:
        try:
            numbers = int(
                input(f"How many numbers do you want to {what_function}? "))
            if numbers > 0:
                return numbers
            else:
                ClearAndLogo()
                print("Please enter a positive integer.")
        except ValueError:
            ClearAndLogo()
            print(
                "Invalid input! Please enter a valid integer for the number of numbers.")
