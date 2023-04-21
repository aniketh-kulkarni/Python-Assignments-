# Program to throw an exception with your own message
# This program will throw a custom exception with a custom message
class CustomException(Exception):
    def __init__(self, message):
        self.message = message

try:
    raise CustomException("This is a custom exception with a custom message")
except CustomException as e:
    print(e.message)
