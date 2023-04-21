# Write a function to add integer values of an array

def array_sum(arr):
    sum = 0
    for i in arr:
        sum += i
    print("The sum of the array is:", sum)
my_array = [1, 2, 3, 4, 5]
array_sum(my_array)

