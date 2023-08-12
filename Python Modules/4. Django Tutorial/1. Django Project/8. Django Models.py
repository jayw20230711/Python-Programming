"""
Django Models

A Django model is a table in your database.

SQLite Database
When we created the Django project, we got an empty SQLite database. It was created in the myworld root folder.
We will use this database in this tutorial.

Create Table (Model)
To create a new table, we must create a new model.

In the /members/ folder, open the models.py file. It is almost empty by default, with only an import statement
and a comment:     members/models.py:

  from django.db import models

  # Create your models here.

To add a Members table in our database, start by creating a Members class, and describe the table fields in it:
members/models.py:

from django.db import models

class Members(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)


The first field, "firstname" is a Text field, and will contain the first name of the members.
The second field, "lastname" is also a Text field, with the members' last name.
Both "firstname" and "lastname" is set up to have a maximum of 255 characters.

Then navigate to the /myworld/ folder and run this command:

--->py manage.py makemigrations members

Which will result in this output:

Migrations for 'members':
  members\migrations\0001_initial.py
    - Create model Members

Django creates a file with any new changes and stores the file in the /migrations/ folder.

Next time you run py manage.py migrate Django will create and execute an SQL statement, based on the content of the
new file in the migrations folder.

Run the migrate command:
--> py manage.py migrate

Which will result in this output:

Operations to perform:
  Apply all migrations: admin, auth, contenttypes, members, sessions
Running migrations:
  Applying members.0001_initial... OK

The SQL statement created from the model is:

CREATE TABLE "members_members" (
"id" INT NOT NULL PRIMARY KEY AUTOINCREMENT,
"firstname" varchar(255) NOT NULL,
"lastname" varchar(255) NOT NULL);

Now you have a Members table in you database!

"""