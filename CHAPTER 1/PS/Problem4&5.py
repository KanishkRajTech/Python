# 4)Write a python program to print the contents of a directory using the os module. Search online for the function which does that. 

# 5) Label the program written in problem 4 with comments.  
import os

# Specify the directory path (use '.' for current directory) you want to list show
directory_path = '/'

# List the contents of the directory
try:
    contents = os.listdir(directory_path)
    print(f"Contents of '{directory_path}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print("The directory does not exist.")
except PermissionError:
    print("You do not have permission to access this directory.")
