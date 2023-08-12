"""
Django cycle Tag

Cycles
The cycle tag allows you to do different tasks for different iterations.

The cycle tag takes arguments, the first iteration uses the first argument, the second iteration uses the second
argument etc.

{% cycle 'lightblue' 'pink' 'yellow' 'coral' 'grey' %}

If you want to have a new background color for each iteration, you can do that with the cycle tag:

# template.html
<!DOCTYPE html>
<html>
<body>

<ul>
  {% for x in members %}
    <li style='background-color:{% cycle 'lightblue' 'pink' 'yellow' 'coral' 'grey' %}'>
      {{ x.firstname }}
    </li>
  {% endfor %}
</ul>

<p>In views.py you can see how to import and fetch members from the database.</p>

</body>
</html>

# views.py
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Members

def testing(request):
  mymembers = Members.objects.all().values()
  template = loader.get_template('template.html')
  context = {
    'members': mymembers,
  }
  return HttpResponse(template.render(context, request))


If the cycle reaches the end of the arguments, it starts over:

# template.html
<!DOCTYPE html>
<html>
<body>

<ul>
  {% for x in members %}
    <li style='background-color:{% cycle 'lightblue' 'pink' %}'>
      {{ x.firstname }}
    </li>
  {% endfor %}
</ul>

<p>In views.py you can see how to import and fetch members from the database.</p>

</body>
</html>

# views.py
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Members

def testing(request):
  mymembers = Members.objects.all().values()
  template = loader.get_template('template.html')
  context = {
    'members': mymembers,
  }
  return HttpResponse(template.render(context, request))


If the cycle reaches the end of the arguments, it starts over:
# template.html
<!DOCTYPE html>
<html>
<body>

<ul>
  {% for x in members %}
    <li style='background-color:{% cycle 'lightblue' 'pink' %}'>
      {{ x.firstname }}
    </li>
  {% endfor %}
</ul>

<p>In views.py you can see how to import and fetch members from the database.</p>

</body>
</html>

# views.py
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Members

def testing(request):
  mymembers = Members.objects.all().values()
  template = loader.get_template('template.html')
  context = {
    'members': mymembers,
  }
  return HttpResponse(template.render(context, request))


Cycle Arguments as Variable
In the first example the argument values was displayed directly in the cycle, but you can also keep the argument
values in a variable, and use it later:

# Store the color values in a variable named bgcolor, and use it as a background color later in the loop:
# template.html
<ul>
  {% for x in members %}
    {% cycle 'lightblue' 'pink' 'yellow' 'coral' 'grey' as bgcolor silent %}
    <li style='background-color:{{ bgcolor }}'>
      {{ x.firstname }}
    </li>
  {% endfor %}
</ul>


#views.py
def testing(request):
  mymembers = Members.objects.all().values()
  template = loader.get_template('template.html')
  context = {
    'members': mymembers,
  }
  return HttpResponse(template.render(context, request))


Did you notice the silent keyword? Make sure you add this, or else the argument values will be displayed
twice in the output:

# template.html
<ul>
  {% for x in members %}
    {% cycle 'lightblue' 'pink' 'yellow' 'coral' 'grey' as bgcolor %}
    <li style='background-color:{{ bgcolor }}'>
      {{ x.firstname }}
    </li>
  {% endfor %}
</ul>


Reset Cycle
You can force the cycle to restart by using the {% resetcycle %} tag:
# Restart the cycle after 3 cycles:

# template.html
<ul>
  {% for x in members %}
    {% cycle 'lightblue' 'pink' 'yellow' 'coral' 'grey' as bgcolor silent %}
    {% if forloop.counter == 3 %}
      {% resetcycle %}
    {% endif %}
    <li style='background-color:{{ bgcolor }}'>
      {{ x.firstname }}
    </li>
  {% endfor %}
</ul>

"""