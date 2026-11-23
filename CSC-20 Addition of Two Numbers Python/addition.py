# This file contains the arithmetic functions shared by the console, GUI, and web apps.
# Run the console calculator with: python3 addition.py


# Return the sum of the two numbers.
def add(num1, num2):

    sum = num1 + num2

    return sum


# Return the first number minus the second number.
def substract(num1, num2):

    sum = num1 - num2

    return sum


# Return the product of the two numbers.
def multiply(num1, num2):

    sum = num1 * num2

    return sum


# Return the whole-number quotient, rounding toward zero for negative results.
# The caller must check that num2 is not zero before calling this function.
def divide(num1, num2):

    quotient = abs(num1) // abs(num2)
    if (num1 < 0) != (num2 < 0):
        quotient = -quotient

    sum = quotient

    return sum


# Ask for two integers and an operation, then display the calculation.
def main():

    # Ask for the first number and store it in num1.
    print("Please input the first digit: ")
    num1 = int(input())

    # Ask for the second number and store it in num2.
    print("Please input the second digit: ")
    num2 = int(input())

    # Ask the user to choose an operation using an lowercase word.
    print("Please input the operation you want to perform (add, subtract, multiply, divide): ")
    chosenOperation = input()

    # Check which operation the user entered and call the matching method.
    if chosenOperation == "add":
        sum = add(num1, num2)
        print("The sum is: " + str(sum))
    elif chosenOperation == "subtract":
        difference = substract(num1, num2)
        print("The difference is: " + str(difference))
    elif chosenOperation == "multiply":
        product = multiply(num1, num2)
        print("The product is: " + str(product))
    elif chosenOperation == "divide":
        quotient = divide(num1, num2)
        print("The quotient is: " + str(quotient))


# Run the console interface only when this file is started directly.
if __name__ == "__main__":
    main()
