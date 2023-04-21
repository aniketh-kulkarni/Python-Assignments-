#Function to insert an element at a specific position in the array:
def insert_element(arr, element, position):
    new_arr = arr[:position] + [element] + arr[position:]
    print("The element", element, "has been inserted at position", position, "in the array")
    return new_arr
my_array = [1, 2, 3, 4, 5]
new_array = insert_element(my_array, 6, 2)  # The element 6 has been inserted at position 2 in the array
print(new_array)  # [1, 2, 6, 3, 4, 5]
