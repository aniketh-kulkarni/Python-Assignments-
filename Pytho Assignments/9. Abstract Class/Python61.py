# 1. Create an abstract class with abstract and non-abstract methods.
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass
    
    def eat(self):
        print("Animal is eating.")

# 2. Create a sub class for an abstract class.
class Cat(Animal):
    def speak(self):
        print("Meow")

    def purr(self):
        print("Purrrr")

# 3. Create an instance for the child class in child class and call abstract methods
my_cat = Cat()
my_cat.speak() # Output: Meow

# 4. Create an instance for the child class in child class and call non-abstract methods show in python
my_cat.eat() # Output: Animal is eating.
my_cat.purr() # Output: Purrrr
