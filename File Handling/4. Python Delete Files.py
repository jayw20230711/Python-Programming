"""
Python Delete File

Delete a File
To delete a file, you must import the OS module, and run its os.remove() function:
"""
os.remove("demofile2.txt")
os.remove("demofile3.txt")

"""
Check if File exist:
To avoid getting an error, you might want to check if the file exists before you try 
to delete it:
"""
if os.path.exists("demofile2.txt"):
    os.remove("demofile2.txt")
else:
    print("The file does not exist")

"""
Delete Folder
To delete an entire folder, use the os.rmdir() method:

Note: You can only remove empty folders.
"""
if os.path.exists("myfolder"):
    os.rmdir("myfolder")
else:
    print("Folder does not exist")
