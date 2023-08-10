"""
Built-in Data Types
In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

Text Type       :	str
Numeric Types   :	int, float, complex
Sequence Types  :	list, tuple, range
Mapping Type    :	dict
Set Types       :	set, frozenset
Boolean Type    :	bool
Binary Types    :	bytes, bytearray, memoryview

HOW TO FIND THE DATA TYPE:
You can get the data type of any object by using the type() function:
"""

x = 5
print(type(x))      # <class 'int'>

"""
SETTING THE DATA TYPE:
In Python, the data type is set when you assign a value to a variable:
"""
x = "Hello World"
""" display x: """
print(x)

""" display the data type of x: """
print(type(x))              # <class 'str'>

""" INT """
x = 20
print(type(x))

""" FLOAT """
x = 20.5
print(type(x))              # <class 'float'>

""" COMPLEX """
x = 1j
print(type(x))                  # <class 'complex'>

""" LIST """
x = ["apple", "banana", "cherry"]
print(type(x))                  # <class 'list'>

""" TUPLE """
x = ("apple", "banana", "cherry")
print(type(x))                  # <class 'tuple'>

""" RANGE """
x = range(6)
print(x)                 # OUTPUT -> range(0, 6)
print(type(x))           # <class 'range'>

""" DICT  =  DICTIONARY """
x = {"name": "John", "age": 36}
print(x)
print(type(x))          # <class 'dict'>

""" SET """
x = {"apple", "banana", "cherry"}
print(x)                    # {'banana', 'cherry', 'apple'}    -- set does not have an order when printing
print(type(x))              # <class 'set'>

""" FROZENSET """
x = frozenset({"apple", "banana", "cherry"})
print(x)                    # frozenset({'banana', 'cherry', 'apple'})
print(type(x))              # <class 'frozenset'>

""" BOOL  = BOOLEAN """
x = True
print(x)
print(type(x))              # <class 'bool'>

""" BYTES """
x = b"Hello"
print(x)                    # b'Hello'
print(type(x))              # <class 'bytes'>

""" BYTEARRAY """
x = bytearray(5)
print(x)                    # bytearray(b'\x00\x00\x00\x00\x00')
print(type(x))              # <class 'bytearray'>

"""  MEMORY VIEW  """
x = memoryview(bytes(5))
print(x)                    # <memory at 0x000002096FF9F700>
print(type(x))              # <class 'memoryview'>

"""
SPECIFYING THE SPECIFIC DATA TYPE: 
If you want to specify the data type, you can use the following constructor functions:
"""

x = str("Hello World")
print(x)
print(type(x))          # <class 'str'>

x = int(20)
print(x)
print(type(x))          # <class 'int'>

x = float(20.5)
print(x)
print(type(x))          # <class 'float'>

x = complex(1j)
print(x)
print(type(x))          # <class 'complex'>

x = list(("apple", "banana", "cherry"))
print(x)
print(type(x))         # <class 'list'>

x = tuple(("apple", "banana", "cherry"))
print(x)
print(type(x))          # <class 'tuple'>

x = range(6)
print(x)
print(type(x))          # <class 'range'>

x = dict(name="John", age=36)
print(x)
print(type(x))          # <class 'dict'>

x = set(("apple", "banana", "cherry"))
print(x)
print(type(x))          # <class 'set'>

x = frozenset(("apple", "banana", "cherry"))
print(x)
print(type(x))              # <class 'frozenset'>

x = bool(5)
print(x)
print(type(x))          # <class 'bool'>

x = bool(-5)
print(x)                # True
print(type(x))

x = bool(0)
print(x)                # False
print(type(x))

x = bytes(5)
print(x)
print(type(x))

x = bytearray(5)
print(x)
print(type(x))

x = memoryview(bytes(5))
print(x)
print(type(x))
