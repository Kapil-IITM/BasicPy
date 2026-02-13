# Simple Calculator

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operator = input("Enter operation (+, -, *, /, **, %):- ")

if operator == "+":
    print(f"Sum of {num1} and {num2} is {num1 + num2}")
elif operator == "-":
    print(f"Difference between {num1} and {num2} is {num1 - num2}")
elif operator == "*":
    print(f"Product of {num1} and {num2} is {num1 * num2}")
elif operator == "/":
    if num2 != 0:
        print(f"{num1} divided by {num2} is {num1 / num2}")
    else:
        print("Error: Division by zero!")
elif operator == "**":
    print(f"{num1} raised to {num2} is {num1 ** num2}")
elif operator == "%":
    if num2 != 0:
        print(f"Remainder of {num1} divided by {num2} is {num1 % num2}")
    else:
        print("Error: Modulo by zero!")
else:
    print("Invalid operation!")
