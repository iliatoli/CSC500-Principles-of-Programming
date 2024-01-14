# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 16:26:06 2024

@author: iliat
"""

def main():
    # Asking the user to input two numbers
    num1 = float(input("Enter first number (num1): "))
    num2 = float(input("Enter second number (num2): "))

    # Ensuring num2 is not zero for division
    if num2 == 0:
        print("Division by zero is not allowed.")
        return

    # Calculating the multiplication and division
    multiplication = num1 * num2
    division = num1 / num2

    # Displaying the results
    print("Multiplication of the numbers: ", multiplication)
    print("Division of the numbers: ", division)

if __name__ == "__main__":
    main()
