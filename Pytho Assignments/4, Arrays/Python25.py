#Function to test if array contains a specific value
def contains_value(arr, value):
    for i in arr:
        if i == value:
            print("The array contains the value", value)
            return True
    print("The array does not contain the value", value)
    return False
my_array = [1, 2, 3, 4, 5]
contains_value(my_array, 3)  # The array contains the value 3
