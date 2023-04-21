# Method to find the number of even and odd numbers in an array

def count_even_odd(arr):
    even_count = 0
    odd_count = 0
    for i in arr:
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    print("Number of even numbers:", even_count)
    print("Number of odd numbers:", odd_count)
    return (even_count, odd_count)
my_array = [1, 2, 3, 4, 5, 6]
even_odd_counts = count_even_odd(my_array)  # Number of even numbers: 3, Number of odd numbers: 3
print(even_odd_counts)  # (3, 3)
