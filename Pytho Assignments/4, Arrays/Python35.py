# Method to find the second smallest number in an array
def find_second_smallest(arr):
    smallest = float('inf')
    second_smallest = float('inf')
    i = 0
    while i < len(arr):
        if arr[i] < smallest:
            second_smallest = smallest
            smallest = arr[i]
        elif arr[i] < second_smallest and arr[i] != smallest:
            second_smallest = arr[i]
        i += 1
    return second_smallest

# Example usage
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
second_smallest = find_second_smallest(arr)
print(second_smallest) # Output: 2

