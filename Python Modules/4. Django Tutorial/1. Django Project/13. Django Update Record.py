"""
Django Update Record

Updating Records
To update a record, we need the ID of the record, and we need a template with an interface that let us change
the values.

First we need to make some changes in the index.html template.

Modify Template
Start by adding a link for each member in the table:  members/templates/index.html:

<h1>Members</h1>

<table border="1">
{% for x in mymembers %}
<tr>
<td><a href="update/{{ x.id }}">{{ x.id }}</a></td>
<td>{{ x.firstname }}</td>
<td>{{ x.lastname }}</td>
<td><a href="delete/{{ x.id }}">delete</a>
</tr>
{% endfor %}
</table>

<p>
<a href="add/">Add member</a>
</p>

The link goes to a view called update with the ID of the current member.

View
Next, add the update view in the members/views.py file:

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Members

def index(request):
  mymembers = Members.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'mymembers': mymembers
  }
  return HttpResponse(template.render(context, request))

def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))

 def addrecord(request):
  first = request.POST['first']
  last = request.POST['last']
  member = Members(firstname=first, lastname=last)
  member.save()

return HttpResponseRedirect(reverse('index'))

def delete(request, id):
  member = Members.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('index'))

def update(request, id):
  mymember = Members.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

The update view does the following:
 - Gets the id as an argument.
 - Uses the id to locate the correct record in the Members table.
 - loads a template called update.html.
 - Creates an object containing the member.
 - Sends the object to the template.
 - Outputs the HTML that is rendered by the template.

New Template
Add a new template in the templates folder, named update.html:
members/templates/update.html:

<h1>Update member</h1>

<form action="updaterecord/{{ mymember.id }}" method="post">
{% csrf_token %}
First Name:<br>
<input name="first" value="{{ mymember.firstname }}">
<br><br>
Last Name:<br>
<input name="last" value="{{ mymember.lastname }}">
<br><br>
<input type="submit" value="Submit">
</form>


The template contains an HTML form with the values from the selected member.

Note: Django requires this line in the form:
{% csrf_token %}
to handle Cross Site Request Forgeries in forms where the method is POST.

URLs
Add a path() function in the members/urls.py file, that points the url 127.0.0.1:8000/members/update/ to the right
location, with the ID as a parameter:
members/urls.py:

from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('add/', views.add, name='add'),
  path('add/addrecord/', views.addrecord, name='addrecord'),
  path('delete/<int:id>', views.delete, name='delete'),
  path('update/<int:id>', views.update, name='update'),
]

In the browser, click the ID of the member you want to change and the result cause error.


What Happens on Submit?
Did you notice the action attribute in the HTML form? The action attribute specifies where to send the form data, in
this case the form data will be sent to:
updaterecord/{{ mymember.id }}, so we must add a path() function in the members/urls.py file that points to the
right view:
members/urls.py:

from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('add/', views.add, name='add'),
  path('add/addrecord/', views.addrecord, name='addrecord'),
  path('delete/<int:id>', views.delete, name='delete'),
  path('update/<int:id>', views.update, name='update'),
  path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
]



Code for Updating Records
So far we have made the user interface, and we point the URL to the view called updaterecord, but we have not made
the view yet.

Make sure you add the updaterecord view in the in the members/views.py file:

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

def delete(request, id):
  member = Members.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('index'))

def update(request, id):
  mymember = Members.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  first = request.POST['first']
  last = request.POST['last']
  member = Members.objects.get(id=id)
  member.firstname = first
  member.lastname = last
  member.save()
  return HttpResponseRedirect(reverse('index'))


The updaterecord function will update the record in the members table with the selected ID.

Try to update a record and see how it works:


"""