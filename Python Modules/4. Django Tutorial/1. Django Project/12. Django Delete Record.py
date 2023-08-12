"""
Django Delete Record

Deleting Records
To delete a record we do not need a new template, but we need to make some changes to the members template.

Of course, you can chose how you want to add a delete button, but in this example, we will add a "delete" link for
each record in a new table column.

The "delete" link will also contain the ID of each record.

Modify Template
Add a "delete" column in the members template: members/templates/index.html:

<h1>Members</h1>

<table border="1">
{% for x in mymembers %}
  <tr>
  <td>{{ x.id }}</td>
  <td>{{ x.firstname }}</td>
  <td>{{ x.lastname }}</td>
  <td><a href="delete/{{ x.id }}">delete</a></td>
  </tr>
{% endfor %}
</table>

<p>
<a href="add/">Add member</a>
</p>


URLs
The "delete" link in the HTML table points to 127.0.0.1:8000/members/delete/ so we will add a path() function in the
members/urls.py file, that points the url to the right location, with the ID as a parameter:
members/urls.py:

from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('add/', views.add, name='add'),
  path('add/addrecord/', views.addrecord, name='addrecord'),
  path('delete/<int:id>', views.delete, name='delete'),
]


Code for Deleting Records
Now we need to add a new view called delete in the members/views.py file:  members/views.py:

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


The delete view does the following:
 - Gets the id as an argument.
 - Uses the id to locate the correct record in the Members table.
 - Deletes that record.
 - Redirects the user back to the index view.

Click on the "delete" link for Jane Doe, and see the result:

"""