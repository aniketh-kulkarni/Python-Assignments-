# To define a static variable in a class and change it within the class
class MyClass:
    my_static_variable = 42

MyClass.my_static_variable = 21 # changing the static variable for the class
print(MyClass.my_static_variable)
