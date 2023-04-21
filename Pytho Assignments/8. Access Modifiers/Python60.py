'''Create a class with PUBLIC fields and methods. 
Access the public methods and fields from any class in the same package or different 
package'''
# Define a class with public fields and methods
class MyClass:
    # Public field
    my_public_field = "This is a public field"
    
    # Public method
    def my_public_method(self):
        print("This is a public method")

# Access the public fields and methods from a different module
from my_module import MyClass

# Access the public field
print(MyClass.my_public_field)

# Access the public method
my_object = MyClass()
my_object.my_public_method()
