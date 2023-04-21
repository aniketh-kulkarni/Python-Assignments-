# Program to check whether a number is even or odd using switch
num = 10

switch = num % 2

switcher = {
    0: "Even",
    1: "Odd"
}

print(switcher.get(switch, "Invalid number"))
