# Simple Python Calculator
# By: Your Name

import math

def calculator():
    print("==== PYTHON CALCULATOR ====")
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Square (x^2)")
    print("6. Square Root (√x)")
    print("7. Exit")

    while True:
        choice = input("\nEnter your choice (1-7): ")

        if choice == '1':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result:", a + b)

        elif choice == '2':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result:", a - b)

        elif choice == '3':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result:", a * b)

        elif choice == '4':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            if b == 0:
                print("Error: Cannot divide by zero!")
            else:
                print("Result:", a / b)

        elif choice == '5':
            a = float(input("Enter a number: "))
            print("Square:", a ** 2)

        elif choice == '6':
            a = float(input("Enter a number: "))
            if a < 0:
                print("Error: Cannot take square root of negative number!")
            else:
                print("Square Root:", math.sqrt(a))

        elif choice == '7':
            print("Thank you for using calculator!")
            break

        else:
            print("Invalid choice! Please enter a number 1 to 7.")

# Start Program
calculator()