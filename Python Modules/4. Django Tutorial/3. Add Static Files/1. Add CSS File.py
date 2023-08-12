"""
Django Adding CSS file

Add a Static CSS File
When building web applications, you probably want to add some static files like images or css files.

Start by creating a folder named static in your project, the same place where you created the templates folder:

myworld
    manage.py
    myworld/
    members/
        templates/
        static/

Add a file in the static folder, name it myfirst.css:
myworld
    manage.py
    myworld/
    members/
        templates/
        static/
            myfirst.css


Open the CSS file and insert the following:
# members/static/myfirst.css:
body {
  background-color: lightblue;
  font-family: verdana;
}


Modify the Template
Now you have a css file, with some css properties that will style an HTML page. The next step will be to include this file in a HTML template:

Open the HTML file and add the following:
{% load static %}

And:
<link rel="stylesheet" href="{% static 'myfirst.css' %}">

Restart the server for the changes to take effect:
--->py manage.py runserver

Example
members/templates/template.html:

{% load static %}
<!DOCTYPE html>
<html>
<link rel="stylesheet" href="{% static 'myfirst.css' %}">
<body>

{% for x in fruits %}
  <h1>{{ x }}</h1>
{% endfor %}

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


Note: For some reason, make sure that DEBUG = True in the settings.py file.
"""