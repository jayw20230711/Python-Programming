"""
Django Views

Views
Django views are Python functions that takes http requests and returns http response, like HTML documents.

A web page that uses Django is full of views with different tasks and missions.

Views are usually put in a file called views.py located on your app's folder.

There is a views.py in your members folder that looks like this:
members/views.py:
    from django.shortcuts import render

    # Create your views here.

Find it and open it, and replace the content with this:

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world!")


This is a simple example on how to send a response back to the browser.
But how can we execute the view? Well, we must call the view via a URL.

URLs
Create a file named urls.py in the same folder as the views.py file, and type this code in it:
members/urls.py :

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

The urls.py file you just created is specific for the members application. We have to do some routing in the root
directory myworld as well. This may seem complicated, but for now, just follow the instructions below.

There is a file called urls.py on the myworld folder, open that file and add the include module in the import
statement, and also add a path() function in the urlpatterns[] list, with arguments that will route users that comes
in via 127.0.0.1:8000/members/.

Then your file will look like this: myworld/urls.py:

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('members/', include('members.urls')),
    path('admin/', admin.site.urls),
]

If the server is not running, navigate to the /myworld folder and execute this command in the command prompt:
--->py manage.py runserver


In the browser window, type 127.0.0.1:8000/members/ in the address bar.
"""