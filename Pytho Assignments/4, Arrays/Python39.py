# Program to remove duplicate elements and return the new array

def remove_duplicates(arr):
    new_arr = list(set(arr))
    print("The array with duplicate elements removed:")
    return new_arr

# Example usage
my_array = [1, 2, 3, 4, 5, 2, 4, 6]
new_array = remove_duplicates(my_array)  # The array with duplicate elements removed: [1, 2, 3, 4, 5, 6]
print(new_array) 
