"""
File: subtract_numbers.py
-------------------------
This program gets two real-values from the user and prints
the first number minus the second number.
"""

def main():
    """
    Calculate the first number minus the second number.
    """

    # Tell the user what the program does
    print("This program subtracts one number from another.")

    # Prompt user to enter two numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Calculate first number minus second number
    answer = num1 - num2

    # Give result to user
    print("The result is " + str(answer))


if __name__ == '__main__':
    main()
