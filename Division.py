from ClearAndLogo import ClearAndLogo


class Division:
    def __init__(self, numbers):
        self.numbers = numbers
        self.division_result = None  # To store the final division result
        self.is_float = False  # Flag to check if any float was entered

        for i in range(numbers):
            while True:
                input_number = input(f"Enter number {i+1}: ")

                # Try to convert input to float first, since float can hold both int and float values
                try:
                    # Convert input to float
                    input_number = float(input_number)
                except ValueError:
                    print("Please enter a valid number.")
                    continue  # Ask for input again if invalid

                # Check for division by zero (only for divisors after the first number)
                if i > 0 and input_number == 0:
                    print("Error: Division by zero is not allowed.")
                    continue  # Ask for input again if zero is entered as a divisor

                # If it's the first number, initialize division_result
                if i == 0:
                    self.division_result = input_number
                else:
                    self.division_result /= input_number  # Divide by the input number

                # Check if the number is a float
                if not input_number.is_integer():
                    self.is_float = True

                break  # Exit the input loop if valid input is provided

        # Print the final result
        if self.is_float:
            print(
                f"The result of the division is: {float(self.division_result)}")
        else:
            print(
                f"The result of the division is: {int(self.division_result)}")
