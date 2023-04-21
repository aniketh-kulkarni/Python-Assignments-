# Program to generate NoSuchFieldException
# This program will generate a NoSuchFieldException by attempting to access a non-existent field of an object
class MyClass:
    def init(self, a):
        self.a = a
        obj = MyClass(10)
        try:
            b = obj.b
            except AttributeError:
            print("Error: Attribute not found")

