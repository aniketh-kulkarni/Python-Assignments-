# Program with multiple catch blocks
# This program will catch multiple types of exceptions using multiple catch blocks
try:
    a = 10
    b = 0
    result = a/b
    print(result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")
except ValueError:
    print("Error: Invalid input value")
except Exception:
    print("Error: Something went wrong")
