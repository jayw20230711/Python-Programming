"""
Adding Template

Adding a Template to the Application
In the previous chapter, we managed to display the content of a database table in a web page:

To add some HTML around the values, we will create a template for the application.

All templates must be located in the templates folder off your app, if you have not already created a templates folder,
do it now.

In the templates folder, create a file named index.html, with the following content: members/templates/index.html:

<h1>Members</h1>

<table border="1">
{% for x in mymembers %}
<tr>
<td>{{ x.id }}</td>
<td>{{ x.firstname }}</td>
<td>{{ x.lastname }}</td>
</tr>
{% endfor %}
</table>

Did you notice the {%  %} and {{  }} parts? They are called template tags.

Template tags allows you to perform logic and render variables in your templates, you will learn more about template
tags later.

Modify the View
Change the index view to include the template:  members/views.py:

from django.http import HttpResponse
from django.template import loader
from .models import Members

def index(request):
  mymembers = Members.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

The index view does the following:

Creates a mymembers object with all the values of the Members model.
Loads a the index.html template.
Creates an object containing the mymember object.
Sends the object to the template.
Outputs the HTML that is rendered by the template.

In the browser window, type 127.0.0.1:8000/members/ in the address bar.

"""