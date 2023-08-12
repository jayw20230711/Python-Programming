"""
Django if Tag

If Statement
An if statement evaluates a variable and executes a block of code if the value is true.

Example:

{% if greeting == 1 %}
  <h1>Hello</h1>
{% endif %}


Elif
The elif keyword says "if the previous conditions were not true, then try this condition".

Example:

{% if greeting == 1 %}
  <h1>Hello</h1>
{% elif greeting == 2 %}
  <h1>Welcome</h1>
{% endif %}


Else
The else keyword catches anything which isn't caught by the preceding conditions.

Example:

{% if greeting == 1 %}
  <h1>Hello</h1>
{% elif greeting == 2 %}
  <h1>Welcome</h1>
{% else %}
  <h1>Goodbye</h1>
{% endif %}


Operators
The above examples uses the == operator, which is used to check if a variable is equal to a value, but there are many
other operators you can use, or you can even drop the operator if you just want to check if a variable is not empty:

# template.html
<!DOCTYPE html>
<html>
<body>

{% if greeting %}
  <h1>Hello</h1>
{% endif %}

<p>In views.py you can see what the greeting variable looks like.</p>

</body>
</html>


# views.py
from django.http import HttpResponse
from django.template import loader

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'greeting': 2,
  }
  return HttpResponse(template.render(context, request))


==
Is equal to.


!=
Is not equal to.


<
Is less than.

<=
Is less than, or equal to.

>
Is greater than.


>=
Is greater than, or equal to.


and
To check if more than one condition is true.

# template.html
<!DOCTYPE html>
<html>
<body>

{% if greeting == 1 and day == "Friday" %}
  <h1>Hello Weekend!</h1>
{% endif %}

<p>In views.py you can see what the variables look like.</p>

</body>
</html>


# views.py
from django.http import HttpResponse
from django.template import loader

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'greeting': 1,
    'day': 'Friday',
  }
  return HttpResponse(template.render(context, request))


or
To check if one of the conditions is true.

# template.html
<!DOCTYPE html>
<html>
<body>

{% if greeting == 1 or greeting == 5 %}
  <h1>Hello</h1>
{% endif %}

<p>In views.py you can see what the greeting variable looks like.</p>

</body>
</html>


# views.py
from django.http import HttpResponse
from django.template import loader

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'greeting': 1,
  }
  return HttpResponse(template.render(context, request))



and/or
Combine and and or.

# template.html
<!DOCTYPE html>
<html>
<body>

{% if greeting == 1 and day == "Friday" or greeting == 5 %}
  <h1>Hello Weekend!</h1>
{% endif %}

<p>In views.py you can see what the variables look like.</p>

</body>
</html>


# views.py
from django.http import HttpResponse
from django.template import loader

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'greeting': 5,
    'day': 'Friday',
  }
  return HttpResponse(template.render(context, request))


Parentheses are not allowed in if statements in Django, so when you combine and and or operators, it is important to
know that parentheses are added for and but not for or.

Meaning that the above example is read by the interpreter like this:

{% if (greeting == 1 and day == "Friday") or greeting == 5 %}


in
To check if a certain item is present in an object.

# template.html
<!DOCTYPE html>
<html>
<body>

{% if 'Banana' in fruits %}
  <h1>Hello</h1>
{% else %}
  <h1>Goodbye</h1>
{% endif %}

<p>In views.py you can see what the fruits variable looks like.</p>

</body>
</html>


# views.py
from django.http import HttpResponse
from django.template import loader

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],
  }
  return HttpResponse(template.render(context, request))



not in
To check if a certain item is not present in an object.

Example :
{% if 'Banana' not in fruits %}
  <h1>Hello</h1>
{% else %}
  <h1>Goodbye</h1>
{% endif %}


is
Check if two objects are the same.

This operator is different from the == operator, because the == operator checks the values of two objects, but the
is operator checks the identity of two objects.

In the view we have two objects, x and y, with the same values:

Example
views.py:

from django.http import HttpResponse
from django.template import loader

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'x': ['Apple', 'Banana', 'Cherry'],
    'y': ['Apple', 'Banana', 'Cherry'],
  }
  return HttpResponse(template.render(context, request))


The two objects have the same value, but is it the same object?

{% if x is y %}
  <h1>YES</h1>
{% else %}
  <h1>NO</h1>               # they are not the same object, two seperate objects
{% endif %}


Let us try the same example with the == operator instead:  Answer is YES, because they contain the same values.

{% if x == y %}
  <h1>YES</h1>
{% else %}
  <h1>NO</h1>
{% endif %}



How can two objects be the same? Well, if you have two objects that points to the same object, then the is operator
evaluates to true:

We will demonstrate this by using the {% with %} tag, which allows us to create variables in the template:

# template.html
<!DOCTYPE html>
<html>
<body>

{% with var1=x var2=x %}
  {% if var1 is var2 %}
    <h1>YES</h1>
  {% else %}
    <h1>NO</h1>
  {% endif %}
{% endwith %}

<p>The x variable is created in views.py, and both var1 and var2 points to x.</p>

</body>
</html>


# views.py
from django.http import HttpResponse
from django.template import loader

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'x': ['Apple', 'Banana', 'Cherry'],
    'y': ['Apple', 'Banana', 'Cherry'],
  }
  return HttpResponse(template.render(context, request))


is not
To check if two objects are not the same.  x and y are not the same object.

{% if x is not y %}
  <h1>YES</h1>
{% else %}
  <h1>NO</h1>
{% endif %}







"""