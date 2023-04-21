# Program to handle the Arithmetic exception using try-catch block
# This program will handle the Arithmetic Exception by catching it and displaying an error message
a = 10
b = 0
try:
    result = a/b
    print(result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")
