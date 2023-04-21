# Here's an example dictionary with 5 key-value pairs of student ID and name
student_dict = {
    101: 'John Smith',
    102: 'Jane Doe',
    103: 'Bob Johnson',
    104: 'Emily Brown',
    105: 'David Lee'
}
# Adding a new key-value pair to the dictionary:
student_dict[106] = 'Sarah Johnson'
# Updating an existing value in the dictionary:
student_dict[103] = 'Robert Johnson'
# Accessing a value in the dictionary:
print(student_dict[104]) # Output: 'Emily Brown'
# Creating a nested loop dictionary:
student_courses = {
    101: {
        'Math': 'A',
        'English': 'B',
        'History': 'C'
    },
    102: {
        'Math': 'B',
        'English': 'A',
        'History': 'A'
    },
    103: {
        'Math': 'C',
        'English': 'B',
        'History': 'B'
    }
}
# Accessing values in a nested loop dictionary:
print(student_courses[102]['English']) # Output: 'A'
# Printing the keys present in a particular dictionary:
print(student_dict.keys()) # Output: dict_keys([101, 102, 103, 104, 105, 106])
# Deleting a value from a dictionary:
del student_dict[106]



