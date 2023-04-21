# Program with a method that throws an exception, called in the main class without try block
# This program defines a method that throws an exception, and calls it in the main class without try block
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    else:
        return a/b

# Call the divide function with valid and invalid arguments
print(divide(10, 2))
print(divide(10, 0))  # This will generate a ZeroDivisionError exception
