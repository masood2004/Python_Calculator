from ClearAndLogo import ClearAndLogo


class Addition:
    def __init__(self, numbers):
        self.numbers = numbers
        self.sum = 0
        self.is_float = False  # Flag to check if any float was entered

        for i in range(numbers):
            input_number = input(f"Enter number {i+1}: ")

            # Try to convert input to float first, since float can hold both int and float values
            try:
                input_number = float(input_number)  # Convert input to float
            except ValueError:
                print("Please enter a valid number.")
                return  # Exit if invalid input is encountered

            if input_number.is_integer():  # Check if the number is an integer
                # Convert to int if it's a whole number
                input_number = int(input_number)
            else:
                self.is_float = True  # Set flag if any input is a float

            self.sum += input_number  # Add the number to the sum

        # If any float number was entered, the sum will be a float
        if self.is_float:
            print(f"The sum of the numbers is: {float(self.sum)}")
        else:
            print(f"The sum of the numbers is: {int(self.sum)}")
