from Addition import Addition
from Division import Division
from Multiplication import Multiplication
from ask_numbers import ask_numbers
from ClearAndLogo import ClearAndLogo
from AskFunction import AskFunction
from Subtraction import Subtraction

ClearAndLogo()


def main_calculator():
    while True:
        function_type = AskFunction().ask()
        if function_type == 1:
            Addition(ask_numbers("add"))
        elif function_type == 2:
            Subtraction(ask_numbers("subtract"))
        elif function_type == 3:
            Multiplication(ask_numbers("multiply"))
        elif function_type == 4:
            Division(ask_numbers("divide"))
        else:
            ClearAndLogo()
            print("Invalid input. Please try again.")

        # Ask the user if they want to continue
        continue_calc = input(
            "Do you want to perform another calculation? (y/n) ").lower()
        if continue_calc != "y":
            ClearAndLogo()
            print("Goodbye!")
            break
        else:
            ClearAndLogo()  # Clear the screen for the next calculation


# Start the calculator
main_calculator()
