"""
Django include Tag

Include
The include tag allows you include a template inside the current template.

This is useful when you have a block of content that are the same for many pages.

# footer.html:
<p>You have reach the bottom of this page, thank you for your time.</p>

# template.html:
<!DOCTYPE html>
<html>
<body>

<h1>Hello</h1>

<p>This page contains a footer in a template.</p>

{% include 'footer.html' %}

<p>Check out the two templates to see what they look like, and views.py to see the reference to the child template.</p>

</body>
</html>

# views.py

def testing(request):
  template = loader.get_template('template.html')
  return HttpResponse(template.render())


Variables in Include
You can send variables into the template by using the with keyword.

In the include file, you refer to the variables by using the {{ variablename }} syntax:

# mymenu.html:
<div>HOME | {{ me }} | ABOUT | FORUM | {{ sponsor }}</div>

# template.html:
<!DOCTYPE html>
<html>
<body>

{% include mymenu.html with me="TOBIAS" sponsor="W3SCHOOLS" %}

<h1>Welcome</h1>

<p>This is my webpage</p>

<p>Check out mymenu.html to see the HTML content of the include.</p>

</body>
</html>




"""