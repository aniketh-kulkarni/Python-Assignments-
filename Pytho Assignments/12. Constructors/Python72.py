# Write a program which illustrates the concept of attributes of a constructor show the codes in python
class ExampleClass:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1 # public attribute
        self._arg2 = arg2 # protected attribute
        self.__arg3 = 0 # private attribute
    
    def get_arg3(self):
        return self.__arg3
    
    def set_arg3(self, arg3):
        self.__arg3 = arg3
    
ec = ExampleClass("hello", "world")
print(ec.arg1) # output: "hello"
print(ec._arg2) # output: "world"
print(ec.get_arg3()) # output: 0 (private attribute is not directly accessible)
ec.set_arg3(42)
print(ec.get_arg3()) # output: 42 (private attribute can be accessed indirectly via getter/setter methods)
