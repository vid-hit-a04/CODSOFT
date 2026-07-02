# Simple Calculator Program

print("Welcome to Simple Calculator")
print("Operations available: +  -  *  /")

# Taking input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operation = input("Enter operation (+, -, *, /): ")

# Performing calculation
if operation == "+":
    result = num1 + num2
    print("Result:", result)

elif operation == "-":
    result: float = num1 - num2
    print("Result:", result)

elif operation == "*":
    result = num1 * num2
    print("Result:", result)

elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Division by zero is not allowed.")

else:
    print("Invalid operation selected. Please choose +, -, *, or /.")