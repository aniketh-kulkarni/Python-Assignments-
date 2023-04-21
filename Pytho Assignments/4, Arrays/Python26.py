#Function to remove a specific element from an array:
def remove_element(arr, element):
    new_arr = []
    for i in arr:
        if i != element:
            new_arr.append(i)
    print("The element", element, "has been removed from the array")
    return new_arr
my_array = [1, 2, 3, 4, 5]
new_array = remove_element(my_array, 3)  # The element 3 has been removed from the array
print(new_array)  # [1, 2, 4, 5]
