# Program with a finally block
# This program demonstrates the use of a finally block to perform cleanup actions
try:
    a = 10
    b = 0
    result = a/b
    print(result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")
finally:
    print("Cleanup: Closing database connection")
