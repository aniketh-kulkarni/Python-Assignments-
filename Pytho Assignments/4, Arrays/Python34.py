# Method to find the second largest number in an array
def find_second_largest(arr):
    largest = arr[0]
    second_largest = arr[0]
    for i in arr:
        if i > largest:
            second_largest = largest
            largest = i
        elif i > second_largest and i != largest:
            second_largest = i
    print("The second largest number in the array is", second_largest)
    return second_largest
my_array = [1, 2, 3, 4, 5, 6]
second_largest = find_second_largest(my_array)  # The second largest number in the array is 5
print(second_largest) 
