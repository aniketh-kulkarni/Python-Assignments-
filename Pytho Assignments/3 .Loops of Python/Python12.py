# Python program to demonstrate the equal and not equal operators
num = int(input("Enter a number: "))
target = 7

while num != target:
    if num < target:
        print("The number is too low")
    else:
        print("The number is too high")
    num = int(input("Enter a new number: "))

print("Congratulations! You guessed the target number!")

