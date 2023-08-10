"""
Open a File on the Server
Assume we have the following file, located in the same folder as Python:

demofile.txt

Hello! Welcome to demofile.txt
This file is for testing purposes.
Good Luck!

The open() function returns a file object, which has a read() method for reading
the content of the file:
"""
f = open("../demofile.txt", "r")
print(f.read())
f.close()

"""
If the file is located in a different location, you will have to specify the file path, like this:

"""
# f = open("C:\\myfiles\welcome.txt", "r")
# print(f.read())


"""
Read Only Parts of the File
By default the read() method returns the whole text, but you can also specify how 
many characters you want to return:

Return the 5 first characters of the file:
"""
print('\nReturn the 5 first characters of the file:')
f = open("../demofile.txt")
print(f.read(5))
f.close()

"""
Read Lines
You can return one line by using the readline() method:
"""
print('\nreturn one line by using the readline() method:')
f = open("../demofile.txt", "r")
print(f.readline())
f.close()

"""
By calling readline() two times, you can read the first two lines:
"""
print('\ncalling readline() two times, you can read the first two lines:')
f = open("../demofile.txt")
print(f.readline())
print(f.readline())
f.close()

"""
By looping through the lines of the file, you can read the whole file, line by line:
"""
f = open("../demofile.txt")
print("Reading the whole file: \n")
for x in f:
    print(x)

f.close()
"""
Note: You should always close your files, in some cases, due to buffering, changes made to a file may not show 
until you close the file.
"""
