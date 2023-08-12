"""
Django Adding JS file

Add a Static JS File
Adding js files in Django project is done exactly the same way as adding css files in Django:

Static files, like css, js, and images, goes in the static folder. If you do not have one, create it in the same
location as you created the templates folder:

myworld
    manage.py
    myworld/
    members/
        templates/
        static/


Add a js file in the static folder, name it myfirst.js:
myworld
    manage.py
    myworld/
    members/
        templates/
        static/
            myfirst.js


Open the JS file and insert the following:
# members/static/myfirst.js:
function myFunction() {
  alert("Hello from a static file!");
}


Modify the Template
Now you have a js file, with a JavaScript function. The next step will be to include this file in a HTML template:

Open the HTML file and add the following:
# members/templates/template.html:
{% load static %}
<!DOCTYPE html>
<html>
<script src="{% static 'myfirst.js' %}"></script>
<body>

<button onclick="myFunction()">Click me!</button>

<p>In myfirst.js you can see the myFunction function.</p>

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

Restart the server for the changes to take effect:

--->py manage.py runserver


Note: For some reason, make sure that DEBUG = True in the settings.py file.

"""