"""
Django Add Record

Adding Records
So far we have created a Members table in our database, and we have inserted five records by writing code in the
Python shell.

We have also made a template that allows us to display the content of the table in a web page.

Now we want to be able to create new members from a web page.


Template
Start by adding a link in the members template:  members/templates/index.html:

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

<p>
<a href="add/">Add member</a>
</p>


check browser for the link.

New Template
Add a new template in the templates folder, named add.html: members/templates/add.html:

<h1>Add member</h1>

<form action="addrecord/" method="post">
{% csrf_token %}
First Name:<br>
<input name="first">
<br><br>
Last Name:<br>
<input name="last">
<br><br>
<input type="submit" value="Submit">
</form>


The template contains an empty HTML form with two input fields and a submit button.

Note: Django requires this line in the form:
{% csrf_token %}
to handle Cross Site Request Forgeries in forms where the method is POST.


View
Next, add a view in the members/views.py file, name the new view add: members/views.py:

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

def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))

URLs
Add a path() function in the members/urls.py file, that points the url 127.0.0.1:8000/members/add/ to the
right location:  members/urls.py:

from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('add/', views.add, name='add'),
]

In the browser, click the "Add member" link.

More URLs
Did you notice the action attribute in the HTML form? The action attribute specifies where to send the form data,
in this case the form data will be sent to addrecord/, so we must add a path() function in the members/urls.py file
that points to the right view:  members/urls.py:

from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('add/', views.add, name='add'),
  path('add/addrecord/', views.addrecord, name='addrecord'),
]

Code for Adding Records
So far we have made the user interface, and we point the URL to the view called addrecord, but we have not made
the view yet.

Make sure you add the addrecord view in the in the members/views.py file:  members/views.py:

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Members

def index(request):
  mymembers = Members.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
  x = request.POST['first']
  y = request.POST['last']
  member = Members(firstname=x, lastname=y)
  member.save()
  return HttpResponseRedirect(reverse('index'))


Changes that are made in the views.py file:

Line 1: import HttpResponseRedirect
Line 3: import reverse

The addrecord view does the following:
 - Gets the first name and last name with the request.POST statement.
 - Adds a new record in the members table.
 - Redirects the user back to the index view.

Try to add a new record and see how it works:


"""