#Function to find the minimum and maximum value of an array:
def find_min_max(arr):
    min_val = arr[0]
    max_val = arr[0]
    for i in arr:
        if i < min_val:
            min_val = i
        if i > max_val:
            max_val = i
    print("The minimum value in the array is", min_val)
    print("The maximum value in the array is", max_val)
    return (min_val, max_val)
my_array = [1, 2, 3, 4, 5]
min_max = find_min_max(my_array)  # The minimum value in the array is 1; The maximum value in the array is 5
print(min_max)  # (1, 5)

