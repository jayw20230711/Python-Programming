"""
Python Bitwise Operators
Bitwise operators are used to compare (binary) numbers:

Operator	Name	                Description
& 	        AND	                    Sets each bit to 1 if both bits are 1
|	        OR	                    Sets each bit to 1 if one of two bits is 1
 ^	        XOR	                    Sets each bit to 1 if only one of two bits is 1
~ 	        NOT	                    Inverts all the bits
<<	        Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
>>	        Signed right shift	    Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off


"""


a = 60   # 0011 1100
b = 12   # 0000 1101
c = 0
c = a & b    # 0011 1100      = 12       - AND
print(c)

c = a | b   # 0011 1101    = 61        - OR
print(c)

c = a ^ b    # 	XOR	Sets each bit to 1 if only one of two bits is 1
print(c)     # 49 = 0011 0001

c = ~ a     # ~ 	NOT	Inverts all the bits
print(c)    # -61 = 1100 0011

c = a << 2  # <<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
print(c)    # 240 = 1111 0000

c = a >> 2   # Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
print(c)     # 15 = 0000 1111

