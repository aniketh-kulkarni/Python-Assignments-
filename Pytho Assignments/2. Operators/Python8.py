# Program for relational operators (<,<==, >, >==)
a = int(input("Enter the First Number:"))
b = int(input("Enter the Second Number:"))
if a<b:
    print("The Largest Value is :",b)
elif a<=b:
    print("The Value of 'a' is :",a)
    print("The Value of 'b' is :",b)
elif a>b:
    print("The Largest Value is :",a)
elif a>=b:
    print("The Value of 'b' is :",b)
    print("The Value of 'a' is :",a)
elif a==b:
    print("Both the values are equal")
else:
    print("The values are invalid")