# Matching a String Against a Regular Expression With matches()
import re

my_string = "Hello World"
result = re.match(r'H\w+', my_string)
print(result.group())
