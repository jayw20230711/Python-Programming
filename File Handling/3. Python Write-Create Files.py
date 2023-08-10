"""
Python File Write

Write to an Existing File
To write to an existing file, you must add a parameter to the open() function:
"a" - Append - will append to the end of the file
"w" - Write - will overwrite any existing content
"""
f = open("../demofile.txt", "a")
f.write("Now the file has more content!")
f.close()

# open and read the file after the appending:
f = open("../demofile.txt")
print(f.read())
f.close()

# Open the file "demofile3.txt" and overwrite the content:
f = open("../demofile.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

# open and read the file after the appending:
f = open("demofile3.txt", "r")
print(f.read())

"""
Create a New File

To create a new file in Python, use the open() method, with one of the following parameters:
"x" - Create - will create a file, returns an error if the file exist
"a" - Append - will create a file if the specified file does not exist
"w" - Write - will create a file if the specified file does not exist

"""

f = open("demofile2.txt", "x")  # Result: a new empty file is created!
f.close()

f = open("demofile2.txt", "w")  # Create a new file if it does not exist:
f.close()

f = open("demofile3.txt", "a")  # will create a file if the specified file does not exist
f.close()
