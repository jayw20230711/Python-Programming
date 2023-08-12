"""
Django QuerySet Order By

Order By
To sort QuerySets, Django uses the order_by() method:

Example
Order the the result alphabetically by firstname:

mydata = Members.objects.all().order_by('firstname').values()

In SQL, the above statement would be written like this:
SELECT * FROM members ORDER BY firstname;

# views.py
from django.http import HttpResponse
from django.template import loader
from .models import Members

def testing(request):
  mydata = Members.objects.all().order_by('firstname').values()
  template = loader.get_template('template.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))


# template.html
<!DOCTYPE html>
<html>
<body>

<p>The queryset object:</p>

{{ mymembers }}

<p>Loop through the items:</p>

<table border='1'>
  <tr>
    <th>ID</th>
    <th>Firstname</th>
    <th>Lastname</th>
  </tr>
  {% for x in mymembers %}
    <tr>
      <td>{{ x.id }}</td>
        <td>{{ x.firstname }}</td>
      <td>{{ x.lastname }}</td>
    </tr>
  {% endfor %}
</table>

</body>
</html>


Output :
The queryset object:

<QuerySet [{'id': 1, 'firstname': 'Emil', 'lastname': 'Refsnes'}, {'id': 4, 'firstname': 'Lene', 'lastname': 'Refsnes'}, {'id': 3, 'firstname': 'Linus', 'lastname': 'Refsnes'}, {'id': 5, 'firstname': 'Stale', 'lastname': 'Refsnes'}, {'id': 13, 'firstname': 'Tobias', 'lastname': 'Refsnes'}]>
Loop through the items:

ID	Firstname	Lastname
1	Emil	Refsnes
4	Lene	Refsnes
3	Linus	Refsnes
5	Stale	Refsnes
13	Tobias	Refsnes


Descending Order
By default, the result is sorted ascending (the lowest value first), to change the direction to descending (the highest
value first), use the minus sign (NOT), - in front of the field name:

Example
Order the the result firstname descending:

mydata = Members.objects.all().order_by('-firstname').values()

In SQL, the above statement would be written like this:
SELECT * FROM members ORDER BY firstname DESC;

# views.py
from django.http import HttpResponse
from django.template import loader
from .models import Members

def testing(request):
  mydata = Members.objects.all().order_by('-firstname').values()
  template = loader.get_template('template.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))

# template.html
<!DOCTYPE html>
<html>
<body>

<p>The queryset object:</p>

{{ mymembers }}

<p>Loop through the items:</p>

<table border='1'>
  <tr>
    <th>ID</th>
    <th>Firstname</th>
    <th>Lastname</th>
  </tr>
  {% for x in mymembers %}
    <tr>
      <td>{{ x.id }}</td>
        <td>{{ x.firstname }}</td>
      <td>{{ x.lastname }}</td>
    </tr>
  {% endfor %}
</table>

</body>
</html>


Output:
The queryset object:

<QuerySet [{'id': 13, 'firstname': 'Tobias', 'lastname': 'Refsnes'}, {'id': 5, 'firstname': 'Stale', 'lastname': 'Refsnes'},
{'id': 3, 'firstname': 'Linus', 'lastname': 'Refsnes'}, {'id': 4, 'firstname': 'Lene', 'lastname': 'Refsnes'},
{'id': 1, 'firstname': 'Emil', 'lastname': 'Refsnes'}]>
Loop through the items:

ID	Firstname	Lastname
13	Tobias	Refsnes
5	Stale	Refsnes
3	Linus	Refsnes
4	Lene	Refsnes
1	Emil	Refsnes


Multiple Order Bys
To order by more than one field, separate the fieldnames with a comma in the order_by() method:

Example
Order the the result first by lastname ascending, then descending on id:

mydata = Members.objects.all().order_by('lastname', '-id').values()


In SQL, the above statement would be written like this:
SELECT * FROM members ORDER BY lastname ASC, id DESC;

# views.py
from django.http import HttpResponse
from django.template import loader
from .models import Members

def testing(request):
  mydata = Members.objects.all().order_by('lastname', '-id').values()
  template = loader.get_template('template.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))


# template.html
<!DOCTYPE html>
<html>
<body>

<p>The queryset object:</p>

{{ mymembers }}

<p>Loop through the items:</p>

<table border='1'>
  <tr>
    <th>ID</th>
    <th>Firstname</th>
    <th>Lastname</th>
  </tr>
  {% for x in mymembers %}
    <tr>
      <td>{{ x.id }}</td>
        <td>{{ x.firstname }}</td>
      <td>{{ x.lastname }}</td>
    </tr>
  {% endfor %}
</table>

</body>
</html>

Output:
The queryset object:

<QuerySet [{'id': 13, 'firstname': 'Tobias', 'lastname': 'Refsnes'}, {'id': 5, 'firstname': 'Stale', 'lastname': 'Refsnes'},
{'id': 4, 'firstname': 'Lene', 'lastname': 'Refsnes'}, {'id': 3, 'firstname': 'Linus', 'lastname': 'Refsnes'},
{'id': 1, 'firstname': 'Emil', 'lastname': 'Refsnes'}]>

Loop through the items:

ID	Firstname	Lastname
13	Tobias	Refsnes
5	Stale	Refsnes
4	Lene	Refsnes
3	Linus	Refsnes
1	Emil	Refsnes




"""