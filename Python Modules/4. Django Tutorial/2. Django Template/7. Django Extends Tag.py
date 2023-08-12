"""
Django extends Tag

Extends
The extends tag allows you to add a parent template for the current template.

This means that you can have one master page that acts like a parent for all other pages:

# mymaster.html:
<html>
<body>

<h1>Welcome</h1>

{% block mymessage %}
{% endblock %}

</body>
</html>

# template.html:
{% extends 'mymaster.html' %}

{% block mymessage %}
  <p>This page has a master page</p>
{% endblock %}

# views.py
def testing(request):
  template = loader.get_template('template.html')
  return HttpResponse(template.render())


You put placeholders in the master template, telling Django where to put which content.

Django uses the {% block %} tag, to create placeholders:

# master.html:
<html>
<body>

{% block myheading %}
{% endblock %}

{% block mymessage %}
{% endblock %}

</body>
</html>


Templates that uses the master template, uses the {% block %} tag to create content that will be displayed in
the placeholder with the same name:
# template.html:

{% extends 'mymaster.html' %}

{% block myheading %}
  <h1>Members</h1>
{% endblock %}

{% block mymessage %}
  <ul>
    {% for x in members %}
      <li>{{ x.firstname }}</li>
    {% endfor %}
  </ul>
{% endblock %}


# views.py

def testing(request):
  mymembers = Members.objects.all().values()
  template = loader.get_template('template.html')
  context = {
    'members': mymembers,
  }
  return HttpResponse(template.render(context, request))

"""