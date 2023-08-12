"""
Django for Tag


For Loops
A for loop is used for iterating over a sequence, like looping over items in an array, a list, or a dictionary.

Loop through the items of a list:

# templates.html
<!DOCTYPE html>
<html>
<body>

{% for x in fruits %}
  <h1>{{ x }}</h1>
{% endfor %}

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


Loop through a list of dictionaries:

# templates.html
<!DOCTYPE html>
<html>
<body>

{% for x in cars %}
  <h1>{{ x.brand }}</h1>
  <p>{{ x.model }}</p>
  <p>{{ x.year }}</p>
{% endfor %}

<p>In views.py you can see what the cars variable looks like.</p>

</body>
</html>


# views.py
from django.http import HttpResponse
from django.template import loader

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'cars': [
      {
        'brand': 'Ford',
        'model': 'Mustang',
        'year': '1964',
      },
      {
        'brand': 'Ford',
        'model': 'Bronco',
        'year': '1970',
      },
      {
        'brand': 'Volvo',
        'model': 'P1800',
        'year': '1964',
      }]
    }
  return HttpResponse(template.render(context, request))


Data From a Model
Data in a model is like a table with rows and columns.

The Members model we created earlier has five rows, and each row has three columns:

id 	 firstname 	 lastname
 1 	 Emil 	     Refsnes
 2 	 Tobias 	 Refsnes
 3 	 Linus 	     Refsnes
 4 	 Lene 	     Refsnes
 5 	 Stalikken 	 Refsnes


When we fetch data from the model, it comes as a QuerySet object, with a similar format as the cars example above: a
list with dictionaries:

<QuerySet [
  {
    'id': 1,
    'firstname': 'Emil',
    'lastname': 'Refsnes'
  },
  {
    'id': 2,
    'firstname': 'Tobias',
    'lastname': 'Refsnes'
  },
  {
    'id': 3,
    'firstname': 'Linus',
    'lastname': 'Refsnes'
  },
  {
    'id': 4,
    'firstname': 'Lene',
    'lastname': 'Refsnes'
  },
  {
    'id': 5,
    'firstname': 'Stalikken',
    'lastname': 'Refsnes'
  }
]>


Loop through items fetched from a database:

{% for x in members %}
  <h1>{{ x.id }}</h1>
  <p>
    {{ x.firstname }}
    {{ x.lastname }}
  </p>
{% endfor %}



Reversed
The reversed keyword is used when you want to do the loop in reversed order.

{% for x in members reversed %}
  <h1>{{ x.id }}</h1>
  <p>
    {{ x.firstname }}
    {{ x.lastname }}
  </p>
{% endfor %}



Empty
The empty keyword can be used if you want to do something special if the object is empty.

# templates.html
<!DOCTYPE html>
<html>
<body>

<ul>
  {% for x in emptytestobject %}
    <li>{{ x.firstname }}</li>
  {% empty %}
    <li>No members</li>
  {% endfor %}
</ul>

<p>In views.py you can see the emptytestobject.</p>

</body>
</html>


# views.py
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'emptytestobject': [],
  }
  return HttpResponse(template.render(context, request))


The empty keyword can also be used if the object does not exist:
# templates.html
<!DOCTYPE html>
<html>
<body>

<ul>
  {% for x in myobject %}
    <li>{{ x.firstname }}</li>
  {% empty %}
    <li>No members</li>
  {% endfor %}
</ul>

<p>In views.py you can see that there is no myobject variable.</p>

</body>
</html>


# views.py
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],
  }
  return HttpResponse(template.render(context, request))


Loop Variables
Django has some variables that are available for you inside a loop:

forloop.counter
forloop.counter0
forloop.first
forloop.last
forloop.parentloop
forloop.revcounter
forloop.revcounter0


forloop.counter
The current iteration, starting at 1.

<!DOCTYPE html>
<html>
<body>

<ul>
  {% for x in fruits %}
    <li>{{ forloop.counter }}</li>                                    # 1, 2, 3, 4, 5
  {% endfor %}
</ul>

<p>In views.py you can see what the fruits object looks like.</p>

</body>
</html>


forloop.counter0
The current iteration, starting at 0.

<!DOCTYPE html>
<html>
<body>

<ul>
  {% for x in fruits %}
    <li>{{ forloop.counter0 }}</li>                     # 0, 1, 2, 3, 4
  {% endfor %}
</ul>

<p>In views.py you can see what the fruits object looks like.</p>

</body>
</html>


forloop.first
Allows you to test if the loop is on its first iteration.

# Draw a blue background for the first iteration of the loop:

<!DOCTYPE html>
<html>
<body>

<ul>
  {% for x in fruits %}
    <li
      {% if forloop.first %}
        style='background-color:lightblue;'
      {% endif %}
    >{{ x }}</li>
  {% endfor %}
</ul>

<p>In views.py you can see what the fruits object looks like.</p>

</body>
</html>


forloop.last
Allows you to test if the loop is on its last iteration.

# Draw a blue background for the last iteration of the loop:

<!DOCTYPE html>
<html>
<body>

<ul>
  {% for x in fruits %}
    <li
      {% if forloop.last %}
        style='background-color:lightblue;'
      {% endif %}
    >{{ x }}</li>
  {% endfor %}
</ul>

<p>In views.py you can see what the fruits object looks like.</p>

</body>
</html>


forloop.revcounter
The current iteration if you start at the end and count backwards, ending up at 1.

<!DOCTYPE html>
<html>
<body>

<ul>
  {% for x in fruits %}
    <li>{{ forloop.revcounter }}</li>
  {% endfor %}
</ul>

<p>In views.py you can see what the fruits object looks like.</p>

</body>
</html>


forloop.revcounter0
The current iteration if you start at the end and count backwards, ending up at 0.

<!DOCTYPE html>
<html>
<body>

<ul>
  {% for x in fruits %}
    <li>{{ forloop.revcounter0 }}</li>
  {% endfor %}
</ul>

<p>In views.py you can see what the fruits object looks like.</p>

</body>
</html>












"""