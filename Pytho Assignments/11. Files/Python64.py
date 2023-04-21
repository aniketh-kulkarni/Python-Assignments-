# Write a program to write text to .txt file using InputStream
with open('filename.txt', 'w') as file:
    text = input('Enter the text to write to the file: ')
    file.write(text)