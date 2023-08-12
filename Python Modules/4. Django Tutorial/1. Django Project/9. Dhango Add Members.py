"""
Django Add Members

Add Records
The Members table is empty, we should add some members to it.

In the next chapters you will learn how to make a user interface that will take care of CRUD operations (Create, Read,
Update, Delete), but for now, let's write Python code directly in the Python interpreter (Python shell) and add some
members in our database, without the user interface.

To open a Python shell, type this command:
--->py manage.py shell

Now we are in the shell, the result should be something like this:

Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
--->>>

At the bottom, after the three >>> write the following:

--> >>>from members.models import Members

Hit [enter] and write this to look at the empty Members table:

--->>>> Members.objects.all()

This should give you an empty QuerySet object, like this:
<QuerySet []>

A QuerySet is a collection of data from a database.
Read more about QuerySets in the Django QuerySet chapter.

Add a record to the table, by executing these two lines:

--->>> member = Members(firstname='Emil', lastname='Refsnes')
--->>> member.save()

Execute this command to see if the Members table got a member:

--->>> Members.objects.all().values()

Hopefully, the result will look like this:

<QuerySet [{'id': 1, 'firstname': 'Emil', 'lastname': 'Refsnes'}]>

Add Multiple Records
You can add multiple records by making a list of Members obejcts, and execute .save() on each entry:

--->>> member1 = Members(firstname='Tobias', lastname='Refsnes')
--->>> member2 = Members(firstname='Linus', lastname='Refsnes')
--->>> member3 = Members(firstname='Lene', lastname='Refsnes')
--->>> member4 = Members(firstname='Stale', lastname='Refsnes')
--->>> members_list = [member1, member2, member3, member4]
--->>> for x in members_list:
--->>> x.save()

Now there are 5 members in the Members table:
--->>> Members.objects.all().values()
<QuerySet [{'id': 1, 'firstname': 'Emil', 'lastname': 'Refsnes'}, {'id': 2, 'firstname': 'Tobias',
'lastname': 'Reftsnes'}, {'id': 3, 'firstname': 'Linus', 'lastname': 'Refsnes'}, {'id': 4,
'firstname': 'Lene', 'lastname': 'Refsnes'}, {'id': 5, 'firstname': 'Stale', 'lastname': 'Refsnes'}]>


View in Browser
We want to see the result in a web page, not in a Python shell environment.
To see the result in a web page, we can create a view for this particular task.

In the members app, open the views.py file, if you have followed the previous chapters of this tutorial, it should
look like this:  members/views.py:

from django.http import HttpResponse
from django.template import loader

def index(request):
  template = loader.get_template('myfirst.html')
  HttpResponse(template.render())

Change the content in the views.py file to look like this instead: members/views.py:

from django.http import HttpResponse
from django.template import loader
from .models import Members

def index(request):
  mymembers = Members.objects.all().values()
  output = ""
  for x in mymembers:
    output += x["firstname"]
  return HttpResponse(output)

As you can see in line 3, the Members model is imported, and the index view does the following:

makes a mymembers object with all the values of the Members model.
Loops through all items in the mymembers object to build a string with all the firstname values.
Returns the string as output to the browser.
See the result in your browser. If you are still in the Python shell, write this command to exit the shell:

--->>> quit()

Navigate to the /myworld/ folder and type this to start the server:

--->py manage.py runserver

In the browser window, type 127.0.0.1:8000/members/ in the address bar.

"""