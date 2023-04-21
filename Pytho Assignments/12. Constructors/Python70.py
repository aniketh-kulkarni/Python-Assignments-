#  Call the constructors(both default and argument constructors) of super class from a child class
class ParentClass:
    def __init__(self):
        print("This is the default constructor of ParentClass")
    
    def __init__(self, arg1):
        print("This is the one argument constructor of ParentClass with arg1 =", arg1)

class ChildClass(ParentClass):
    def __init__(self):
        super().__init__() # Call default constructor of ParentClass
        print("This is the default constructor of ChildClass")
    
    def __init__(self, arg1):
        super().__init__(arg1) # Call one argument constructor of ParentClass with arg1
        print("This is the one argument constructor of ChildClass with arg1 =", arg1)

# Instantiate the child class to call both default and argument constructors of its superclass
cc1 = ChildClass()
cc2 = ChildClass("hello")
