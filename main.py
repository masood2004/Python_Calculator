from art import logo

print(logo)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operation = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

calculating = True

while calculating:
    num1 = float(input("What is your first number? "))
    num2 = float(input("What is your second number? "))
    operand = str(input("What is your operation? ('+' , '-' , '*' , '/') "))
    calculated_num = operation[operand](num1, num2)
    print(f"{num1} {operand} {num2} = {calculated_num}")

    # Main loop to handle continuation of calculation or start a new calculation
    continue_calc = input(
        "'Y' for continue calculation, 'N' for New Calculations, 'exit' for Exit? (y/n/exit): ").lower()

    if continue_calc == "y":
        while continue_calc == 'y':
            # Use the previous result as the new "first number" (calculated_num)
            num3 = float(input(f"What is your next number? (Previous result was {calculated_num}) "))
            operand = str(input("What is your operation? "))
            calculated_num = operation[operand](calculated_num, num3)
            print(f"{calculated_num} {operand} {num3} = {calculated_num}")

            # Prompt user if they want to continue or exit
            continue_calc = input(
                "'Y' for continue calculation, 'N' for New Calculations, 'exit' for Exit? (y/n/exit): ").lower()

    elif continue_calc == "n":
        continue

    elif continue_calc == 'exit':
        calculating = False
        break

    else:
        print("Select a valid option")