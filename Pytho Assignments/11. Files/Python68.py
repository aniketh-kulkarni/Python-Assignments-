# Write a program to check whether a file is having read access and write access permissions show the programs in python
# program to check file access permissions
import os

filename = 'filename.txt'
if os.access(filename, os.R_OK):
    print(f'{filename} has read access')
else:
    print(f'{filename} does not have read access')

if os.access(filename, os.W_OK):
    print(f'{filename} has write access')
else:
    print(f'{filename} does not have write access')
