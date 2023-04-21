# Function to find the duplicate values of an array
def find_duplicates(arr):
    duplicates = []
    for i in arr:
        if arr.count(i) > 1 and i not in duplicates:
            duplicates.append(i)
    if len(duplicates) == 0:
        print("There are no duplicate values in the array")
    else:
        print("The duplicate values in the array are:", duplicates)
    return duplicates
my_array = [1, 2, 3, 4, 5, 2, 4, 6]
duplicates = find_duplicates(my_array)  # The duplicate values in the array are: [2, 4]
print(duplicates) 
