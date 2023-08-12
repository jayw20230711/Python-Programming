"""
Django QuerySet Filter

Django QuerySet Filter
The filter() method is used to filter you search, and allows you to return only the rows that matches the search term.

As we learned in the previous chapter, we can filter on field names like this:


Example
Return only the records where the firstname is 'Emil':

mydata = Members.objects.filter(firstname='Emil').values()


In SQL, the above statement would be written like this:

SELECT * FROM members WHERE firstname = 'Emil';


AND
The filter() method takes the arguments as **kwargs (keyword arguments), so you can filter on more than one field by
sepearting them by a comma.


Example
Return records where lastname is "Refsnes" and id is 2:

# views.py

from django.http import HttpResponse
from django.template import loader
from .models import Members

def testing(request):
  mydata = Members.objects.filter(lastname='Refsnes', id=3).values()
  template = loader.get_template('template.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))


In SQL, the above statement would be written like this:
SELECT * FROM members WHERE   lastname = 'Refsnes' AND id = 3;


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

<QuerySet [{'id': 3, 'firstname': 'Linus', 'lastname': 'Refsnes'}]>
Loop through the items:

ID	Firstname	Lastname
3	Linus	Refsnes


OR
To return records where firstname is Emil or firstname is Tobias (meaning: returning records that matches either query,
not necessarily both) is not as easy as the AND example above.

We can use multiple filter() methods, separated by a pipe | character. The results will merge into one model.

Example
Return records where firstname is either "Emil" or Tobias":

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

# views.py
from django.http import HttpResponse
from django.template import loader
from .models import Members

def testing(request):
  mydata = Members.objects.filter(firstname='Emil').values() | Members.objects.filter(firstname='Tobias').values()
  template = loader.get_template('template.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))


Output :

The queryset object:

<QuerySet [{'id': 1, 'firstname': 'Emil', 'lastname': 'Refsnes'}, {'id': 13, 'firstname': 'Tobias', 'lastname': 'Refsnes'}]>
Loop through the items:

ID	Firstname	Lastname
1	Emil	    Refsnes
13	Tobias	    Refsnes


Another common method is to import and use Q expressions:

Example
Return records where firstname is either "Emil" or Tobias":

# views.py
from django.http import HttpResponse
from django.template import loader
from .models import Members
from django.db.models import Q                # include this

def testing(request):
  mydata = Members.objects.filter(Q(firstname='Emil') | Q(firstname='Tobias')).values()
  template = loader.get_template('template.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))


In SQL, the above statement would be written like this:
SELECT * FROM members WHERE   firstname = 'Emil' OR firstname = 'Tobias';

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

<QuerySet [{'id': 1, 'firstname': 'Emil', 'lastname': 'Refsnes'}, {'id': 13, 'firstname': 'Tobias', 'lastname': 'Refsnes'}]>
Loop through the items:

ID	Firstname	Lastname
1	Emil	Refsnes
13	Tobias	Refsnes


Field Lookups
Django has its own way of specifying SQL statements and WHERE clauses.

To make specific where clasuses in Django, use "Field lookups".

Field lookups are keywords that represents specific SQL keywords.

Example:
.filter(firstname__startswith='L');

Is the same as the SQL statment:
WHERE firstname LIKE 'L%'

The above statement will return records where firstname starts with 'L'.

Field Lookups Syntax
All Field lookup keywords must be specified with the fieldname, followed by two(!) underscore characters, and the keyword.

In our Members model, the statement would be written like this:

Example
Return the records where firstname starts with the letter 'L':

mydata = Members.objects.filter(firstname__startswith='L').values()


# views.py
from django.http import HttpResponse
from django.template import loader
from .models import Members

def testing(request):
  mydata = Members.objects.filter(firstname__startswith='L').values()
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

<QuerySet [{'id': 3, 'firstname': 'Linus', 'lastname': 'Refsnes'}, {'id': 4, 'firstname': 'Lene', 'lastname': 'Refsnes'}]>
Loop through the items:

ID	Firstname	Lastname
3	Linus	Refsnes
4	Lene	Refsnes


Field Lookups Reference
A list of all field look up keywords:

Keyword	            Description
=====================================================================
contains	        Contains the phrase
icontains	        Same as contains, but case-insensitive
date	            Matches a date
day	                Matches a date (day of month, 1-31) (for dates)
endswith	        Ends with
iendswith	        Same as endswidth, but case-insensitive
exact	            An exact match
iexact	            Same as exact, but case-insensitive
in	                Matches one of the values
isnull	            Matches NULL values
gt	                Greater than
gte	                Greater than, or equal to
hour	            Matches an hour (for datetimes)
lt	                Less than
lte	                Less than, or equal to
minute	            Matches a minute (for datetimes)
month	            Matches a month (for dates)
quarter	            Matches a quarter of the year (1-4) (for dates)
range	            Match between
regex	            Matches a regular expression
iregex	            Same as regex, but case-insensitive
second	            Matches a second (for datetimes)
startswith	        Starts with
istartswith	        Same as startswith, but case-insensitive
time	            Matches a time (for datetimes)
week	            Matches a week number (1-53) (for dates)
week_day	        Matches a day of week (1-7) 1 is sunday
iso_week_day	    Matches a ISO 8601 day of week (1-7) 1 is monday
year	            Matches a year (for dates)
iso_year	        Matches an ISO 8601 year (for dates)

"""