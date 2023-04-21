# Write two methods with the same name and same number of parameters of same type show the code in python
class MyClass:
    def my_method(self, x):
        print(f"Method with one parameter: {x}")
        
    def my_method(self, y):
        print(f"Method with one parameter: {y}")
        
# Calling the methods
obj = MyClass()
obj.my_method(1)            # Output: Method with one parameter: 1
obj.my_method(2)            # Output: Method with one parameter: 2
