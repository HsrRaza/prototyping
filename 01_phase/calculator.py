a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
operation = input("Enter an operation (+, -, *, /, //, %, **): ")

def calculator(a ,b , operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a-b
    elif operation == "*":
        return a*b
    elif operation == "/":
        return a/b
    elif operation == "//":
        return a//b
    elif operation == "%":
        return a%b
    elif operation == "**":
        return a**b
    else:
        return "Invalid operation"

print(calculator(a, b, operation))