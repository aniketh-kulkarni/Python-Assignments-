# Python program to print the largest number among three numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

largest = num1
while(num2 > largest or num3 > largest):
    if(num2 > largest):
        largest = num2
    if(num3 > largest):
        largest = num3

print("The largest number is", largest)
