 
# Define the class A
class A:
    def method1(self):
        print("This is method1 of class A.")
        
    def method2(self):
        print("This is method2 of class A.")
        
    def override_method(self):
        print("This is override_method of class A.")
        
# Define the class B
class B(A):
    def method3(self):
        print("This is method3 of class B.")
        
    def method4(self):
        print("This is method4 of class B.")
        
    def override_method(self):
        print("This is override_method of class B.")
        super().override_method()
        
# Define the class C
class C(B):
    def method5(self):
        print("This is method5 of class C.")
        
    def method6(self):
        print("This is method6 of class C.")
        
    def override_method(self):
        print("This is override_method of class C.")
        super().override_method()

# Define the main function
def main():
    # Create an object of class A
    obj_a = A()
    obj_a.method1()
    obj_a.method2()
    obj_a.override_method()
    print("------------------------")
    
    # Create an object of class B
    obj_b = B()
    obj_b.method1()
    obj_b.method2()
    obj_b.method3()
    obj_b.method4()
    obj_b.override_method()
    print("------------------------")
    
    # Create an object of class C
    obj_c = C()
    obj_c.method1()
    obj_c.method2()
    obj_c.method3()
    obj_c.method4()
    obj_c.method5()
    obj_c.method6()
    obj_c.override_method()
    print("------------------------")
    
    # Call the overridden method with super class reference to B and C class's objects
    super(B, obj_b).override_method()
    super(C, obj_c).override_method()

# Call the main function
if __name__ == "__main__":
    main()
