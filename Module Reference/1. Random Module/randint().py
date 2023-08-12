"""
Python Random randint() Method

Definition and Usage
The randint() method returns an integer number selected element from the specified range.

Note: This method is an alias for randrange(start, stop+1).

Syntax
random.randint(start, stop)

Parameter	Description
start	    Required. An integer specifying at which position to start.
stop	    Required. An integer specifying at which position to end.

"""
import random

# returns a number between 3 and 9 (both included)
print(random.randint(3, 9))

u = set()
for v in range(30):
    u.add(random.randint(1, 25))

print(u)

s = set()
s.add(1)
# print(s)
s.update(x for x in range(4, 101))
# print(s)

t = set(x for x in range(1, 66))
# print(t)
t.update(x for x in range(67, 101))
# print(t)

bag1 = list(t)
# print(bag1)

a = set(x for x in range(1, 101))
c = set(bag1)

d = list(a - c)
# print(d)
print(list(a - c))

bag2 = list(s)
a = set(x for x in range(1, 101))
c = set(bag2)
print(list(a - c))

bag3 = list(u)
a = set(x for x in range(1, 26))
c = set(bag3)
print(list(a - c))

