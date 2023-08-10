"""
Python RegEx

A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

RegEx can be used to check if a string contains the specified search pattern.

RegEx Module
Python has a built-in package called re, which can be used to work with Regular Expressions.

Import the re module:

"""
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)

if x:
    print("YES! We have a match!")
else:
    print("No match")

"""
RegEx Functions
The re module offers a set of functions that allows us to search a string for a match:

Function            Description
--------            -------------
findall	            Returns a list containing all matches
search	            Returns a Match object if there is a match anywhere in the string
split	            Returns a list where the string has been split at each match
sub	                Replaces one or many matches with a string
"""

"""
The findall() Function
The findall() function returns a list containing all matches.
"""
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

"""
The list contains the matches in the order they are found.

If no matches are found, an empty list is returned:
"""
txt2 = "TThe rain in Spain"
x = re.findall("Portugal", txt)
print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

"""
The search() Function
The search() function searches the string for a match, and returns a Match object if there is a match.
Ex: <re.Match object; span=(0, 17), match='The rain in Spain'>

If there is more than one match, only the first occurrence of the match will be returned:

"""
txt3 = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position: ", x.start())

"""
If no matches are found, the value None is returned:
"""
txt4 = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)

"""
The split() Function
The split() function returns a list where the string has been split at each match:
"""
txt5 = "The rain in Spain"
x = re.split("\s", txt5)
print(x)

"""
You can control the number of occurrences by specifying the maxsplit parameter:
"""

x = re.split("\s", txt5, 1)
print(x)

"""
The sub() Function
The sub() function replaces the matches with the text of your choice:
"""
txt6 = "The rain in Spain"
x = re.sub("\s", "+", txt6)

print(x)

"""
You can control the number of replacements by specifying the count parameter:
"""
y = re.sub("\s", "+", txt6, 2)
print(y)

"""
Match Object
A Match Object is an object containing information about the search and the result.

Note: If there is no match, the value None will be returned, instead of the Match Object.

"""
txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)  # this will print an object

"""
Metacharacters
Metacharacters are characters with a special meaning:

Character	    Description	                                                                Example	
[]	            A set of characters	                                                        "[a-m]"	
\	            Signals a special sequence (can also be used to escape special characters)	"\d"	
.	            Any character (except newline character)	                                "he..o"	
^	            Starts with	                                                                "^hello"	
$	            Ends with	                                                                "planet$"	
*	            Zero or more occurrences	                                                "he.*o"	
+	            One or more occurrences	                                                    "he.+o"	
?	            Zero or one occurrences	                                                    "he.?o"	
{}	            Exactly the specified number of occurrences	                                "he.{2}o"	
|	            Either or	                                                                "falls|stays"	
()	            Capture and group

"""

txt = "The rain in Spain"
x = re.findall("[a-m]", txt)
print(x)

txt = "That will be 59 dollars"
# Find all digit characters:
x = re.findall("\d", txt)
print(x)

txt = "hello planet"
# Search for a sequence that starts with "he", followed by two (any) characters, and an "o":
x = re.findall("he..o", txt)
print(x)

txt = "hello planet"
# Check if the string starts with 'hello':
x = re.findall("^hello", txt)
print(x)

if x:
    print("Yes, the string starts with 'hello'")
else:
    print("No match")

txt = "hello planet"
# Check if the string ends with 'planet':
x = re.findall("planet$", txt)
print(x)

if x:
    print("Yes, the string ends with 'planet'")
else:
    print("No match")

txt = "hello planet"
# Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":
x = re.findall("he.*o", txt)
print(x)

txt = "hello planet"
# Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":
x = re.findall("he.+o", txt)
print(x)

txt = "hello planet"
# Search for a sequence that starts with "he", followed by 0 or 1  (any) character, and an "o":
x = re.findall("he.?o", txt)
print(x)
# This time we got no match, because there were not zero, not one, but two characters between "he" and the "o"

txt = "hello planet"
# Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":
x = re.findall("he.{2}o", txt)
print(x)

txt = "The rain in Spain falls mainly in the plain!"
# Check if the string contains either "falls" or "stays":
x = re.findall("falls|stays", txt)
print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

"""
Special Sequences
A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:

Character	Description	                                                                                  Example	
\A	        Returns a match if the specified characters are at the beginning of the string	              "\AThe"	
\b	        Returns a match where the specified characters are at the beginning or at the 
            end of a word (the "r" in the beginning is making sure that the string is being 
            treated as a "raw string")	                                                                  r"\bain"
                                                                                                          r"ain\b"	
\B	        Returns a match where the specified characters are present, but NOT at the 
            beginning (or at the end) of a word (the "r" in the beginning is making sure 
            that the string is being treated as a "raw string")	                                          r"\Bain"
                                                                                                          r"ain\B"	
\d	        Returns a match where the string contains digits (numbers from 0-9)	                          "\d"	
\D	        Returns a match where the string DOES NOT contain digits	                                  "\D"	
\s	        Returns a match where the string contains a white space character	                          "\s"	
\S	        Returns a match where the string DOES NOT contain a white space character	                  "\S"	
\w	        Returns a match where the string contains any word characters (characters 
            from a to Z, digits from 0-9, and the underscore _ character)	                              "\w"	
\W	        Returns a match where the string DOES NOT contain any word characters	                      "\W"	
\Z	        Returns a match if the specified characters are at the end of the string	                  "Spain\Z"

"""

txt = "The rain in Spain"
# Check if the string starts with "The":
x = re.findall("\AThe", txt)
print(x)
if x:
    print("Yes, there is a match!")
else:
    print("No match")

txt = "The rain in Spain"
# Check if "ain" is present at the beginning of a WORD:
x = re.findall(r"\bain", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

txt = "The rain in Spain"
# Check if "ain" is present at the end of a WORD:
x = re.findall(r"ain\b", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

txt = "The rain in Spain"
# Check if "ain" is present, but NOT at the beginning of a word:
x = re.findall(r"\Bain", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

txt = "The rain in Spain"
# Check if "ain" is present, but NOT at the end of a word:
x = re.findall(r"ain\B", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

txt = "That will be 59 dollars"
# Find all digit characters:
x = re.findall("\d", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

txt = "The rain in Spain"
# Return a match at every no-digit character:
x = re.findall("\D", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

txt = "The rain in Spain"
# Return a match at every white-space character:
x = re.findall("\s", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

txt = "The rain in Spain"
# Return a match at every NON white-space character:
x = re.findall("\S", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

txt = "The rain in Spain was on 19th Feb_2020"
# Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character):
x = re.findall("\w", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

txt = "The rain in Spain was on 19th Feb _ 2020 ? ! "
# Return a match at every NON word character (characters NOT between a and Z.  Like "!", "?" white-space etc.):
x = re.findall("\W", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

txt = "The rain in Spain"
# Check if the string ends with "Spain":
x = re.findall("Spain\Z", txt)
print(x)
if x:
    print("Yes, there is a match!")
else:
    print("No match")

"""
Sets
A set is a set of characters inside a pair of square brackets [] with a special meaning:

Set	        Description	
[arn]	    Returns a match where one of the specified characters (a, r, or n) are present	
[a-n]	    Returns a match for any lower case character, alphabetically between a and n	
[^arn]	    Returns a match for any character EXCEPT a, r, and n	
[0123]	    Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
[0-9]	    Returns a match for any digit between 0 and 9	
[0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59	
[a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case	
[+]	        In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match 
            for any + character in the string
"""

txt = "The rain in Spain"
# Check if the string has any a, r, or n characters:
x = re.findall("[arn]", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

txt = "The rain in Spain"
# Check if the string has any characters between a and n:
x = re.findall("[a-n]", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

txt = "The rain in Spain"
# Check if the string has other characters than a, r, or n:
x = re.findall("[^arn]", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

"""
The Match object has properties and methods used to retrieve information about the search, and the result:

.span() returns a tuple containing the start-, and end positions of the match.
.string returns the string passed into the function
.group() returns the part of the string where there was a match

Note: If there is no match, the value None will be returned, instead of the Match Object.

Example
Print the position (start- and end-position) of the first match occurrence.

The regular expression looks for any words that starts with an upper case "S":
"""

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())
