"""
Strings
Strings in python are surrounded by either single quotation marks, or double quotation marks.

'hello' is the same as "hello".

You can display a string literal with the print() function:
You can use double or single quotes:
"""
print("Hello")
print('Hello')

a = "Hello"
print(a)

"""
Multiline Strings
You can assign a multiline string to a variable by using three quotes:
"""
a = """Lorem ipsum dolor sit amet, 
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

"""
Or three single quotes:
"""
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

"""
Strings are Arrays
Like many other popular programming languages, strings in Python are arrays of bytes 
representing unicode characters.

However, Python does not have a character data type, a single character is simply a 
string with a length of 1.

Square brackets can be used to access elements of the string.
"""
a = "Hello, World!"
print(a[0])
print(a[1])

"""
Looping Through a String
Since strings are arrays, we can loop through the characters in a string, with a for loop.
"""
for x in "banana":
    print(x)

"""
String Length
To get the length of a string, use the len() function.
"""
a = "Hello, World!"
print(len(a))

"""
Check String
To check if a certain phrase or character is present in a string, we can use the keyword in.
"""
txt = "The best things in life are free!"
print("free" in txt)                        # True

"""
Use it in an if statement:
"""
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")

"""
Check if NOT
To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
"""
txt = "The best things in life are free!"
print("expensive" not in txt)               # True

txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")


"""
Slicing
You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string.
"""
b = "Hello, World!"
print(b[2:5])               # llo


"""
Slice From the Start
By leaving out the start index, the range will start at the first character:
"""
b = "Hello, World!"
print(b[:5])


"""
Slice To the End
By leaving out the end index, the range will go to the end:
"""
b = "Hello, World!"
print(b[2:])

"""
Negative Indexing
Use negative indexes to start the slice from the end of the string:

Example
Get the characters:
From: "o" in "World!" (position -5)
To, but not included: "d" in "World!" (position -2):
"""
b = "Hello, World!"
print(b[-5:-2])         # orl

"""
Python - Modify Strings
Python has a set of built-in methods that you can use on strings.

"""


""" The upper() method returns the string in upper case: """
a = "Hello, World!"
print(a.upper())


""" The lower() method returns the string in lower case: """
a = "Hello, World!"
print(a.lower())

"""
Remove Whitespace
Whitespace is the space before and/or after the actual text, 
and very often you want to remove this space.

The strip() method removes any whitespace from the beginning or the end:
"""
a = " Hello, World! "
print(a.strip())   # returns "Hello, World!"


"""
Replace String
Example
The replace() method replaces a string with another string:
"""
a = "Hello, World!"
print(a.replace("H", "J"))

"""
Split String
The split() method returns a list where the text between the specified separator 
becomes the list items.

The split() method splits the string into substrings if it 
finds instances of the separator:
"""
a = "Hello, World!"
print(a.split(","))   # returns ['Hello', ' World!']


"""
String Concatenation
To concatenate, or combine, two strings you can use the + operator.
"""
a = "Hello"
b = "World"
c = a + b
print(c)
print(a + b)

"""
To add a space between them, add a " ":
"""
a = "Hello"
b = "World"
c = a + " " + b
print(c)
print(a + " " + b)

"""
String Format
As we learned in the Python Variables chapter, we cannot combine strings and 
numbers like this:
age = 36
txt = "My name is John, I am " + age
print(txt)


But we can combine strings and numbers by using the format() method!

The format() method takes the passed arguments, formats them, and places them in 
the string where the placeholders {} are:
"""
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

"""
The format() method takes unlimited number of arguments, and are placed 
into the respective placeholders:
"""
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

"""
You can use index numbers {0} to be sure the arguments 
are placed in the correct placeholders:
"""
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))


"""
Escape Character
To insert characters that are illegal in a string, use an escape character.

An escape character is a backslash \ followed by the character you want to insert.

An example of an illegal character is a double quote inside a string that 
is surrounded by double quotes:
"""
# txt = "We are the so-called "Vikings" from the north."
txt = 'We are the so-called "Vikings" from the north.'
print(txt)

txt = "We are the so-called \"Vikings\" from the north."
print(txt)

"""
Escape Characters
Other escape characters used in Python:

Code	Result	
\'	    Single Quote	
\\	    Backslash	
\n	    New Line	
\r	    Carriage Return	
\t	    Tab	
\b	    Backspace	
\f	    Form Feed	
\ooo	Octal value  
"""
# \xhh	Hex value
txt = 'It\' alright.'
print(txt)

txt = "This will insert one \\ (backslash)."
print(txt)

txt = "Hello\nWorld!"
print(txt)

txt = "Hello\rWorld!"
print(txt)

txt = "Hello\tWorld!"
print(txt)

# This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt)

# A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt)


# A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt)
