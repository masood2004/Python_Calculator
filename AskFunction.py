from ClearAndLogo import ClearAndLogo


class AskFunction:
    def ask(self):
        while True:
            try:
                print("1. Addition")
                print("2. Subtraction")
                print("3. Multiplication")
                print("4. Division")
                function = int(input("Which function do you want to use? "))
                if function == 1:
                    return function
                elif function == 2:
                    return function
                elif function == 3:
                    return function
                elif function == 4:
                    return function
                else:
                    ClearAndLogo()
                    print("Invalid input. Please try again.")
            except ValueError:
                ClearAndLogo()
                print(
                    "Invalid input! Please enter a valid integer for the function choice.")
