#Write a method for increment and decrement operators(++, --)
# Pre-increment
x = 5
y = ++x   # equivalent to x = x + 1; y = x
print("After pre-incrementing, x =", x, "and y =", y)

# Post-increment
x = 9
y = x++   # equivalent to y = x; x = x + 1
print("After post-incrementing, x =", x, "and y =", y)

#Pre-decrement
a = 7
b = --a # equivalent to a = a - 1; b = a
print("After pre-decrementing a =", a "and b = ",b)

#Post-decrememt
a = 15
b = a-- # equivalent to b = a; a = a -  1
print("After post-decrementing a =", a "and b = ",b)
