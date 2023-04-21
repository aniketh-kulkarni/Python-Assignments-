# Program to print gender (Male/Female) program according to given M/F using switch
gender = "M"

switcher = {
    "M": "Male",
    "F": "Female"
}

print(switcher.get(gender, "Invalid gender"))

