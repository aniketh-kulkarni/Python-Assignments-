# Apply private, public, protected and default access modifiers to the constructor
class ExampleClass:
    def __init__(self):
        print("This is the default constructor") # public constructor
    
    def __init__(self, arg1):
        self._arg1 = arg1
        print("This is the one argument constructor with arg1 =", arg1) # protected constructor
    
    def __init__(self, arg1, arg2):
        self.__arg2 = arg2
        print("This is the two argument constructor with arg1 =", arg1, "and arg2 =", arg2) # private constructor

ec1 = ExampleClass() # call default constructor (public)
ec2 = ExampleClass("hello") # call one argument constructor (protected)
ec3 = ExampleClass("hello", "world") # call two argument constructor (private)
