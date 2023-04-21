# To define a static variable in a class and access it through an instance
class MyClass:
    my_static_variable = 42

my_instance = MyClass()
print(my_instance.my_static_variable)
