'''Write a class with a default constructor, one argument constructor and two argument 
constructors. Instantiate the class to call all the constructors of that class from a main 
class
'''

class ExampleClass:
    def __init__(self):
        print("This is the default constructor")
    
    def __init__(self, arg1):
        print("This is the one argument constructor with arg1 =", arg1)
    
    def __init__(self, arg1, arg2):
        print("This is the two argument constructor with arg1 =", arg1, "and arg2 =", arg2)

# Instantiate the class to call all the constructors of that class
ec1 = ExampleClass()
ec2 = ExampleClass("hello")
ec3 = ExampleClass("hello", "world")
