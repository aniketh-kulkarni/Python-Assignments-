# Write a program to read a file stream supports random access
# program to read a file stream that supports random access
with open('filename.txt', 'rb+') as file:
    file.seek(10)
    contents = file.read(5)
    print(contents)
