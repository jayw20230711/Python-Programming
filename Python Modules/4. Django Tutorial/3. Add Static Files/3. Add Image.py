"""
Django Adding Image file

Add an Image File
Adding images files in Django project is done he same way as adding css files or adding js files in Django:

Static files, like css, js, and images, goes in the static folder. If you do not have one, create it in the same
location as you created the templates folder:

myworld
    manage.py
    myworld/
    members/
        templates/
        static/


Add a image file (.png, .jpg, .gif, etc.) in the static folder::

myworld
    manage.py
    myworld/
    members/
        templates/
        static/
            pineapple.jpg


Modify the Template
Now you have a image in the static folder. The next step will be to include this image in a HTML template:

Open the HTML file and add the following:
# members/templates/template.html:
{% load static %}
<!DOCTYPE html>
<html>
<body>

<img src="{% static 'pineapple.jpg' %}">

</body>
</html>


#views.py
from django.http import HttpResponse
from django.template import loader

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],
  }
  return HttpResponse(template.render(context, request))



Note: For some reason, make sure that DEBUG = True in the settings.py file.


"""