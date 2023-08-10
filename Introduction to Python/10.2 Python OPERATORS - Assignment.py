"""
Python Assignment Operators
Assignment operators are used to assign values to variables:

Operator	Example	    Same As
=	        x = 5	    x = 5
+=	        x += 3	    x = x + 3
-=	        x -= 3	    x = x - 3
*=	        x *= 3	    x = x * 3
/=	        x /= 3	    x = x / 3
%=	        x %= 3	    x = x % 3
//=	        x //= 3	    x = x // 3
**=	        x **= 3	    x = x ** 3
&=	        x &= 3	    x = x & 3
|=	        x |= 3	    x = x | 3
^=	        x ^= 3	    x = x ^ 3
>>=	        x >>= 3	    x = x >> 3
<<=	        x <<= 3	    x = x << 3

"""

a = 21
b = 10
c = 0

c += a
print(c)

c *= a
print(c)

c /= a
print(c)

c = 200
c %= a
print(c)

c **= b
print(c)
print(11 ** 10)

a = 21
b = 10
c = 0

a //= b
print(a)


a = 2
b = 3

c **= b             # here  ** mean 2 to the power 3  = 8
print(c)

c //= b  # here // Floor division - division that results into whole number adjusted to the left in the number line
print(c)
