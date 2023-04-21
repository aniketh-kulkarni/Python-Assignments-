'''Create a program to create two class.
1.1. Create a constructor and a method for each class
1.2. Create a __init__.py for adding all packages
1.3. Import the respective packages
1.4. Call each class by creating an object to it 
1.5. Create a program by all the above show the program in python
'''
# file: my_classes.py

class MyClass1:
    def __init__(self, arg1):
        self.arg1 = arg1
        
    def my_method(self):
        print(f"MyClass1 object with arg1 = {self.arg1}")
        
        
class MyClass2:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        
    def my_method(self):
        print(f"MyClass2 object with arg1 = {self.arg1} and arg2 = {self.arg2}")
