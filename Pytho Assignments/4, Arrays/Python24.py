# Program to find the index of an array element
def find_index(arr, element):
    for i in range(len(arr)):
        if arr[i] == element:
            print("The index of", element, "is", i)
            return
    print("Element not found in the array")
my_array = [1, 2, 3, 4, 5]
find_index(my_array, 3)

