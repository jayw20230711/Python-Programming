"""
Django QuerySet Get Data

Get Data
There are different methods to get data from a model into a QuerySet.


The values() Method
The values() method allows you to return each object as a Python dictionary, with the names and values
as key/value pairs:

View
# members/views.py:
from django.http import HttpResponse
from django.template import loader
from .models import Members

def testing(request):
  mydata = Members.objects.all().values()
  template = loader.get_template('template.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))

Template
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

<QuerySet [{'id': 1, 'firstname': 'Emil', 'lastname': 'Refsnes'}, {'id': 2, 'firstname': 'Tobias', 'lastname': 'Reftsnes'},
           {'id': 3, 'firstname': 'Linus', 'lastname': 'Refsnes'}, {'id': 4, 'firstname': 'Lene', 'lastname': 'Refsnes'},
           {'id': 5, 'firstname': 'Stale', 'lastname': 'Refsnes'}]>

Loop through the items:

ID	Firstname	Lastname
1	Emil	Refsnes
2	Tobias	Reftsnes
3	Linus	Refsnes
4	Lene	Refsnes
5	Stale	Refsnes


Return Specific Columns
The values_list() method allows you to return only the columns that you specify.

View
# members/views.py:
from django.http import HttpResponse
from django.template import loader
from .models import Members

def testing(request):
  mydata = Members.objects.values_list('firstname')
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
  {% for x in mymembers %}
    <tr>
      <td>{{ x }}</td>
    </tr>
  {% endfor %}
</table>

</body>
</html>


# Output:
The queryset object:

<QuerySet [('Emil',), ('Tobias',), ('Linus',), ('Lene',), ('Stale',)]>
Loop through the items:

('Emil',)
('Tobias',)
('Linus',)
('Lene',)
('Stale',)


Return Specific Rows
You can filter the search to only return specific rows/records, by using the filter() method.

View
# members/views.py:
from django.http import HttpResponse
from django.template import loader
from .models import Members

def testing(request):
  mydata = Members.objects.filter(firstname='Emil').values()
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



# Output:
The queryset object:

<QuerySet [{'id': 1, 'firstname': 'Emil', 'lastname': 'Refsnes'}]>

Loop through the items:

ID	Firstname	Lastname
1	Emil	    Refsnes



"""