# Write two methods with the same name but different number of parameters of different data type and call the methods
class MyClass:
    def my_method(self, x):
        print(f"Method with integer parameter: {x}")
        
    def my_method(self, x, y):
        print(f"Method with string and integer parameters: {x} and {y}")
        
# Calling the methods
obj = MyClass()
obj.my_method(1)            # Output: Method with string and integer parameters: 1 and default
obj.my_method("hello", 2)   # Output: Method with string and integer parameters: hello and 2
