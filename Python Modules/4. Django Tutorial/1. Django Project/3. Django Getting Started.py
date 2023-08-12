"""
Django Getting Started
To install Django, you must have Python installed, and a package manager like PIP.
PIP is included in Python from version 3.4.

Django Requires Python
To check if your system has Python installed, run this command in the command prompt:
--->python --version

If you do not have PIP installed, you can download and install it from this page: https://pypi.org/project/pip/


Virtual Environment
It is suggested to have a dedicated virtual environment for each Django project, and one way to manage a virtual
environment is venv, which is included in Python.

With venv, you can create a virtual environment by typing this in the command prompt, remember to navigate to where
you want to create your project:

py -m venv myproject

This will set up a virtual environment, and create a folder named "myproject" with subfolders and files, like this:

myproject
    - Include
    - Lib
    - Scripts
    - pyvenv.cfg


Note: You must activate the virtual environment every time you open the command prompt to work on your project


Install Django
Finally, we can install Django.
Remember to install Django while you are in the virtual environment!
Django is installed using pip, with this command:
--->py -m pip install Django

Windows, Mac, or Unix?
You can run this project on either one. There are some small differences, like when writing commands in the command
prompt, Windows uses py as the first word in the command line, while Unix and MacOS use python:

Check Django Version
You can check if Django is installed by asking for its version number like this:
--> django-admin --version

What's Next?
Now you are ready to create a Django project in a virtual environment on your computer.

In the next chapters of this tutorial we will create a Django project and look at the various features of Django and
hopefully make you a Django developer.

"""