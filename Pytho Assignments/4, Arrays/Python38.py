# Method to verify if the array contains two specified elements (12, 23)
def verify_elements(arr):
    if 12 in arr and 23 in arr:
        print("The array contains both 12 and 23")
        return True
    else:
        print("The array does not contain both 12 and 23")
        return False
my_array = [1, 2, 3, 4, 5, 12, 23]
contains_both = verify_elements(my_array)  # The array contains both 12 and 23
print(contains_both)  # True
