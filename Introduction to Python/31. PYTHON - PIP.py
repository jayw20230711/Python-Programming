"""
Python PIP
PIP is a package manager for Python packages, or modules if you like.

Note: If you have Python version 3.4 or later, PIP is included by default.

What is a Package?
A package contains all the files you need for a module.

Modules are Python code libraries you can include in your project.


Check if PIP is Installed
Navigate your command line to the location of Python's script directory, and type the following:

C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip --version

Install PIP
If you do not have PIP installed, you can download and install it from this page: https://pypi.org/project/pip/

Download a Package
Downloading a package is very easy.

Open the command line interface and tell PIP to download the package you want.

Navigate your command line to the location of Python's script directory, and type the following:

C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip install camelcase

Using a Package
Once the package is installed, it is ready to use.

Import the "camelcase" package into your project.

"""
import camelcase

c = camelcase.CamelCase()
txt = "lorem ipsum dolor sit amet"

# This method capitalizes the first letter of each word.
print(c.hump(txt))

"""
Find Packages
Find more packages at https://pypi.org/.

Remove a Package
Use the uninstall command to remove a package:

C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip uninstall camelcase

The PIP Package Manager will ask you to confirm that you want to remove the camelcase package:

Uninstalling camelcase-02.1:
  Would remove:
    c:\users\Your Name\appdata\local\programs\python\python36-32\lib\site-packages\camecase-0.2-py3.6.egg-info
    c:\users\Your Name\appdata\local\programs\python\python36-32\lib\site-packages\camecase\*
Proceed (y/n)?

List Packages
Use the list command to list all the packages installed on your system:

C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip list

"""