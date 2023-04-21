# Function to calculate the average value of an array of integers
def array_average(arr):
    sum = 0
    for i in arr:
        sum += i
    average = sum / len(arr)
    print("The average of the array is:", average)
my_array = [1, 2, 3, 4, 5]
array_average(my_array)
