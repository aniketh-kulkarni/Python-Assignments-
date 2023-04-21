# Write a program to read a file a just to a particular index using seek()
with open('filename.txt', 'rb') as file:
    file.seek(10)
    contents = file.read()
    print(contents)
