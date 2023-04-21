# Function to get the difference between the largest and smallest value in an array
def get_difference(arr):
    max_val = max(arr)
    min_val = min(arr)
    diff = max_val - min_val
    print("The difference between the largest and smallest values in the array is:", diff)
    return diff
my_array = [1, 2, 3, 4, 5, 6]
diff = get_difference(my_array)  # The difference between the largest and smallest values in the array is: 5
print(diff) 
