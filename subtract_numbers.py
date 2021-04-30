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
    
    print("This program subtracts one number from another.")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    answer = num1 - num2

    print("The result is", answer)

if __name__ == '__main__':
    main()
