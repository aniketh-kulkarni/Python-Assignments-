# Program to generate ClassNotFoundException
# This program will generate a ClassNotFoundException by attempting to import a non-existent module
try:
    import nonexistentmodule
except ModuleNotFoundError:
    print("Error: Module not found")
