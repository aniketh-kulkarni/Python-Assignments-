#Define the local and Global variables with the same name and print both variables and 
#understand the scope of the variables
# Define a global variable
myVar = "global"

def myFunction():
    # Define a local variable with the same name
    myVar = "local"
    print("Inside the function, myVar is", myVar)

# Call the function
myFunction()

# Print the global variable
print("Outside the function, myVar is", myVar)
