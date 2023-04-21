# Program to generate IOException
# This program will generate an IOException by attempting to write to a read-only file
try:
    file = open("readonlyfile.txt", "r")
    file.write("This is a test")
    file.close()
except IOError:
    print("Error: File could not be written to")
