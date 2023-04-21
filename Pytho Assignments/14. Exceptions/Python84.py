# Program to generate FileNotFoundException
# This program will generate a FileNotFoundException by attempting to open a non-existent file
try:
    file = open("nonexistentfile.txt", "r")
    file.read()
    file.close()
except FileNotFoundError:
    print("Error: File not found")
