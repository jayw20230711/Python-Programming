"""
Django Template Variables

Template Variables
In Django templates, you can render variables by putting them inside {{ }} brackets:
# template.html:

<!DOCTYPE html>
<html>
<body>

<h1>Hello {{ firstname }}, how are you?</h1>

<p>In views.py you can see how to create the variable.</p>
<p>In template.html you can see how to use the variable.</p>

</body>
</html>


Create Variable in View
The variable firstname in the example above was sent to the template via a view:
# views.py:

from django.http import HttpResponse
from django.template import loader

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'firstname': 'Linus',
  }
  return HttpResponse(template.render(context, request))


As you can see in the view above, we create an object named context and fill it with data, and send it as the
first parameter in the template.render() function.

Create Variables in Template
You can also create variables directly in the template, by using the {% with %} template tag:
# template.html:

<!DOCTYPE html>
<html>
<body>

{% with firstname="Tobias" %}
<h1>Hello {{ firstname }}, how are you?</h1>

</body>
</html>




Data From a Model
The example above showed a easy approach on how to create and use variables in a template.

Normally, most of the external data you want to use in a template, comes from a model.

We have created a model in the previous chapters, called Members, we will use this model in the next chapters of
this tutorial.

To get data from the Members model, we will have to import it in the views file, and extract data from it in the view:
# views.py:

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Members

def testing(request):
  mymembers = Members.objects.all().values()
  template = loader.get_template('template.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))


Now we can use the data in the template:
# template.html:

<ul>
  {% for x in mymembers %}
    <li>{{ x.firstname }}</li>
  {% endfor %}
</ul>


We use the Django template tag {% for %} to loop through the members.



"""