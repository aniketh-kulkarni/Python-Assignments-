'''Create a class with PROTECTED fields and methods. Access these fields and methods 
from any other class in the same package. 
Also, Access the PROTECTED fields and methods from child class located in a different 
package'''
# file: mypackage/myclass.py
class MyClass:
    def __init__(self):
        self._x = 10
        self._y = 20
    
    def _protected_method(self):
        print("This is a protected method.")

class MySubclass(MyClass):
    def __init__(self):
        super().__init__()
    
    def print_fields(self):
        print("x =", self._x)
        print("y =", self._y)
    
    def call_protected_method(self):
        self._protected_method()

# file: otherpackage/otherclass.py
from mypackage.myclass import MyClass, MySubclass

class OtherClass:
    def __init__(self):
        self.obj1 = MyClass()
        self.obj2 = MySubclass()
    
    def print_fields(self):
        print("x =", self.obj1._x)
        print("y =", self.obj1._y)
        self.obj2.print_fields()
    
    def call_protected_method(self):
        self.obj2.call_protected_method()
