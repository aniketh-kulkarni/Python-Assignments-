# Write two methods with the same name but different number of parameters of same type and call the methods 
class MyClass:
    def my_method(self, x):
        print(f"Method with one parameter: {x}")
        
    def my_method(self, x, y):
        print(f"Method with two parameters: {x} and {y}")
        
# Calling the methods
obj = MyClass()
obj.my_method(1)            # Output: Method with two parameters: 1 and 2
obj.my_method(1, 2)         # Output: Method with two parameters: 1 and 2
