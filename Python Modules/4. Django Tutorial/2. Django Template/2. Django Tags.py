"""
Django Template Tags

In Django templates, you can perform programming logic like executing if statements and for loops.

These keywords, if and for, are called "template tags" in Django.

To execute template tags, we surround them in {% %} brackets.
# template.html
<!DOCTYPE html>
<html>
<body>

{% if greeting == 1 %}
  <h1>Hello</h1>
{% else %}
  <h1>Bye</h1>
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



Django Code
The template tags are a way of telling Django that here comes something else than plain HTML.

The template tags allows us to to do some programming on the server before sending HTML to the client.

# template.html
<!DOCTYPE html>
<html>
<body>

<ul>
  {% for x in mymembers %}
    <li>{{ x.firstname }}</li>
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
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))



Tag Reference
A list of all template tags:

Tag	                Description
----------------------------------------------------
autoescape	        Specifies if autoescape mode is on or off
block	            Specifies a block section
comment	            Specifies a comment section
csrf_token	        Protects forms from Cross Site Request Forgeries
cycle	            Specifies content to use in each cycle of a loop
debug	            Specifies debugging information
extends	            Specifies a parent template
filter	            Filters content before returning it
firstof	            Returns the first not empty variable
for	                Specifies a for loop
if	                Specifies a if statement
ifchanged	        Used in for loops. Outputs a block only if a value has changed since the last iteration
include	            Specifies included content/template
load	            Loads template tags from another library
lorem	            Outputs random text
now	                Outputs the current date/time
regroup	            Sorts an object by a group
resetcycle	        Used in cycles. Resets the cycle
spaceless	        Removes whitespace between HTML tags
templatetag	        Outputs a specified template tag
url 	            Returns the absolute URL part of a URL
verbatim	        Specifies contents that should not be rendered by the template engine
widthratio	        Calculates a width value based on the ration between a given value and a max value
with	            Specifies a variable to use in the block


"""