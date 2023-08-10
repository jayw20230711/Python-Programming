"""
String Methods
Python has a set of built-in methods that you can use on strings.

Note: All string methods returns new values. They do not change the original string.

Method	                Description
--------------------------------------------------------------------------------
capitalize()	        Converts the first character to upper case
casefold()	            Converts string into lower case
center()	            Returns a centered string
count()	                Returns the number of times a specified value occurs in a string
encode()	            Returns an encoded version of the string
endswith()	            Returns true if the string ends with the specified value
expandtabs()	        Sets the tab size of the string
find()	                Searches the string for a specified value and returns the position of where it was found
format()	            Formats specified values in a string
format_map()	        Formats specified values in a string
index()	                Searches the string for a specified value and returns the position of where it was found
isalnum()	            Returns True if all characters in the string are alphanumeric
isalpha()	            Returns True if all characters in the string are in the alphabet
isdecimal()	            Returns True if all characters in the string are decimals
isdigit()	            Returns True if all characters in the string are digits
isidentifier()	        Returns True if the string is an identifier
islower()	            Returns True if all characters in the string are lower case
isnumeric()	            Returns True if all characters in the string are numeric
isprintable()	        Returns True if all characters in the string are printable
isspace()	            Returns True if all characters in the string are whitespaces
istitle()	            Returns True if the string follows the rules of a title
isupper()	            Returns True if all characters in the string are upper case
join()	                Joins the elements of an iterable to the end of the string
ljust()	                Returns a left justified version of the string
lower()	                Converts a string into lower case
lstrip()	            Returns a left trim version of the string
maketrans()	            Returns a translation table to be used in translations
partition()	            Returns a tuple where the string is parted into three parts
replace()	            Returns a string where a specified value is replaced with a specified value
rfind()	                Searches the string for a specified value and returns the last position of where it was found
rindex()	            Searches the string for a specified value and returns the last position of where it was found
rjust()	                Returns a right justified version of the string
rpartition()	        Returns a tuple where the string is parted into three parts
rsplit()	            Splits the string at the specified separator, and returns a list
rstrip()	            Returns a right trim version of the string
split()	                Splits the string at the specified separator, and returns a list
splitlines()	        Splits the string at line breaks and returns a list
startswith()	        Returns true if the string starts with the specified value
strip()	                Returns a trimmed version of the string
swapcase()	            Swaps cases, lower case becomes upper case and vice versa
title()	                Converts the first character of each word to upper case
translate()	            Returns a translated string
upper()	                Converts a string into upper case
zfill()	                Fills the string with a specified number of 0 values at the beginning


"""


mystring = "hello world"
print("mystring : ", mystring)
print("Capitalise the string :", mystring.capitalize())         # Capitalise the string : Hello world

mystring = "I am saying hello world"
print("lower case string :", mystring.lower())                  # lower case string : i am saying hello world

newstr = "I Would Like To Go Now"
print("new string :", newstr)
print("case fold :", newstr.casefold())                         # case fold : i would like to go now

print("printing newstr :\n")
print(newstr)
print("center the newstr with 40 chars :\n")
print(newstr.center(40))
# The encode() method encodes the string, using the specified encoding. If no encoding is specified, UTF-8 will be used.
newstr = "My name is Ståle"
print("\nencode the newstr :", newstr.encode(errors="replace"))
print(newstr.encode(encoding="ascii", errors="backslashreplace"))
print(newstr.encode(encoding="ascii", errors="ignore"))
print(newstr.encode(encoding="ascii", errors="namereplace"))
print(newstr.encode(encoding="ascii", errors="replace"))
print(newstr.encode(encoding="ascii", errors="xmlcharrefreplace"))

# The endswith() method returns True if the string ends with the specified value, otherwise False.
newstr = "I Would Like To Go Now"
print("\nnewstr end with . ? : ", newstr.endswith("."))
print(newstr)

# The expandtabs() method sets the tab size to the specified number of whitespaces.
txt = "H\te\tl\tl\to"
print("\nprint txt : ", txt)
x = txt.expandtabs(8)
print("expanded 8 tab width :\n")
print(x)
print(txt.expandtabs(8))

# The find() method finds the first occurrence of the specified value.
# The find() method returns -1 if the value is not found.
# The find() method is almost the same as the index() method, the only difference is that the index() method raises
# an exception if the value is not found.
print("\nFind the word 'Go' in the newstr :")
print(newstr.find("Go"))
print("\nFind the word 'will' in the newstr :")
x = newstr.find("will")
if x == -1:
    print("word not found in the string : ", newstr)
else:
    print(newstr.find("will"))

# The format() method formats the specified value(s) and insert them inside the string's placeholder.
txt = "\nFor only {price:.2f} dollars!"
ftxt = txt.format(price=49)
print(ftxt)
txt1 = "My name is {fname}, I'm {age}".format(fname="John", age=36)
print(txt1)
txt2 = "My name is {0}, I'm {1}".format("John", 36)
print(txt2)
txt3 = "My name is {}, I'm {}".format("John", 36)
print(txt3)

# The index() method finds the first occurrence of the specified value.
# The index() method raises an exception if the value is not found.
# x=newstr.index("Am")
try:
    # print(newstr.index("Go"))
    print(newstr.index("Am"))
except ValueError:
    print("ValueError: substring not found")
except RuntimeError:
    print("something went wrong")

# The isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z)
# and numbers (0-9).
txt = "I Would Like To Go Now !"
print("Is the string alphanumeric : ", txt.isalnum())
print(txt)

# The isalpha() method returns True if all the characters are alphabet letters (a-z).
print("Is the string alphabetic only :", txt.isalpha())

# The isascii() method returns True if all the characters are ascii characters  (a-z).
if txt.isascii():
    print("String contains ascii chars only\n")
else:
    print("all characters are not ascii")

# The isdecimal() method returns True if all the characters are decimals (0-9).
# This method is used on unicode objects.
a = "\u0030"  # unicode for 0
b = "\u0047"  # unicode for G
print("\u0030 is unicode for 0 : ", a.isdecimal())
print("\u0047 is unicode for G : ", b.isdecimal())

# The isdigit() method returns True if all the characters are digits, otherwise False.
txt = "50034-"
if txt.isdigit():
    print("\nall chars are digits : " + txt, txt.isdigit())
else:
    print("\ncontain non digit chars : " + txt, txt.isdigit())

# The isidentifier() method returns True if the string is a valid identifier, otherwise False.
# A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9),
# or underscores (_). A valid identifier cannot start with a number, or contain any spaces.
a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"
print("\nValid identifier or not : ")
print(a, a.isidentifier())
print(b, b.isidentifier())
print(c, c.isidentifier())
print(d, d.isidentifier())

# The islower() method returns True if all the characters are in lower case, otherwise False.
# Numbers, symbols and spaces are not checked, only alphabet characters.
txt = "hello world!"
print("\ncheck is lower ? \n" + txt + " - is lower case ?", txt.islower())
txt = "!!hello world"
print(txt + " - is lower case ? ", txt.islower())

a = "Hello world!"
b = "hello 123"
c = "mynameisPeter"
print(a + " - ", a.islower())
print(b + " - ", b.islower())
print(c + " - ", c.islower())

# The isnumeric() method returns True if all the characters are numeric (0-9), otherwise False.
# Exponents, like ² and ¾ are also considered to be numeric values.
# "-1" and "1.5" are NOT considered numeric values, because all the characters in the string must be numeric,
# and the - and the . are not.

a = "\u0030"  # unicode for 0
b = "\u00B2"  # unicode for &sup2;
c = "10km2"
d = "-1"
e = "1.5"
print("\ncheck is numeric ? ")
print(a + " - ", a.isnumeric())
print(b + " - ", b.isnumeric())
print(c + " - ", c.isnumeric())
print(d + " - ", d.isnumeric())
print(e + " - ", e.isnumeric())

# The isprintable() method returns True if all the characters are printable, otherwise False.
# Example of none printable character can be carriage return and line feed.
txt = "Hello!\nAre you #1?"
x = txt.isprintable()
print("Hello!\\nAre you #1?" + " - is printable ? ", x)
