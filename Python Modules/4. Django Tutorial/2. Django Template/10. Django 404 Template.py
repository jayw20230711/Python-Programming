"""
Django 404 (page not found)

Page Not Found
If you try to access a page that do not exist (a 404 error), Django directs you to a built-in view that handles 404 errors.

You will learn how to customize this 404 view later in this chapter, but first, just try to request a page that does not exist.

In the browser window, type 127.0.0.1:8000/masfdfg/ in the address bar.

You will get one of two results:

1:
Not Found

The requested resource was not found on this server.


2:
Page not found (404)
Request Method:	GET
Request URL:	http://127.0.0.1:8000/masfdfg/
Using the URLconf defined in myworld.urls, Django tried these URL patterns, in this order:

members/
admin/
The current path, masfdfg/, didn’t match any of these.

You’re seeing this error because you have DEBUG = True in your Django settings file. Change that to False, and
Django will display a standard 404 page.




If you got the first result, you got directed to the built-in Django 404 template.

If you got the second result, then DEBUG = True, and you must set it to False to get directed to the 404 template.

This is done in the settings.py file, in the project folder, in our case the myworld folder, were you also have to
specify the host name where your project runs from:

Set the debug property to False, and allow the project to run from your local host:

myworld/settings.py:

.
.
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1']



###
Important: When DEBUG = False, Django requires you to specify the hosts you will allow this Django project to run from.

In production, this should include your domain name:

ALLOWED_HOSTS = ['127.0.0.1', 'yourdomain.com']


In the browser window, type 127.0.0.1:8000/masfdfg/ in the address bar, and you will get the built-in 404 template:

Not Found
The requested resource was not found on this server.


Customize the 404 Template
Django will look for a file named 404.html in the templates folder, and display it when there is a 404 error.

Create a file in the template folder and name it 404.html:

# templates/404.html:
<!DOCTYPE html>
<html>
<title>Wrong address</title>
<body>

<h1>Ooops!</h1>

<h2>I cannot find the file you requested!</h2>

</body>
</html>



In the browser window, type 127.0.0.1:8000/masfdfg/ in the address bar, and you will get the customized 404 template:

Ooops !
I cannot find the file you requested!






"""