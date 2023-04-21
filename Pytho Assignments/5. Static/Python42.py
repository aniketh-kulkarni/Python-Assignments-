# To define a static variable in a class and change it within an instance
class MyClass:
    my_static_variable = 42

my_instance = MyClass()
my_instance.my_static_variable = 21 # changing the static variable for the instance
print(MyClass.my_static_variable) # Output: 42 (class static variable is not affected)
print(my_instance.my_static_variable)
