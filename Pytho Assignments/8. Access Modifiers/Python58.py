'''Create a class with PRIVATE fields, private method and a main method. Print the fields 
in main method. Call the private method in main method.'''
class MyClass:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    
    def __private_method(self):
        print("This is a private method.")

    def print_fields(self):
        print("x =", self.__x)
        print("y =", self.__y)

    def call_private_method(self):
        self.__private_method()

class MySubclass(MyClass):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.__z = z

    def print_fields(self):
        super().print_fields()
        print("z =", self.__z)

obj = MyClass(10, 20)
obj.print_fields()
obj.call_private_method()

obj2 = MySubclass(1, 2, 3)
obj2.print_fields()
