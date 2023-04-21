# Program to find the common values between two arrays
def find_common_values(arr1, arr2):
    common = []
    for i in arr1:
        if i in arr2 and i not in common:
            common.append(i)
    if len(common) == 0:
        print("There are no common values between the arrays")
    else:
        print("The common values between the arrays are:", common)
    return common
my_array1 = [1, 2, 3, 4, 5]
my_array2 = [3, 4, 5, 6, 7]
common_values = find_common_values(my_array1, my_array2)  # The common values between the arrays are: [3, 4, 5]
print(common_values)  
