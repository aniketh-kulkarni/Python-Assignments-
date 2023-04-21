#Function to copy an array to another array:
def copy_array(arr):
    new_arr = arr.copy()
    print("The original array has been copied to a new array")
    return new_arr
my_array = [1, 2, 3, 4, 5]
new_array = copy_array(my_array)  # The original array has been copied to a new array
print(new_array)  # [1, 2, 3, 4, 5]
