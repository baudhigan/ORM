# Ex02 Django ORM Web Application
# Date:
# AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

# ENTITY RELATIONSHIP DIAGRAM
## DESIGN STEPS
## STEP 1:
Clone the problem from GitHub

## STEP 2:
Create a new app in Django project

## STEP 3:
Enter the code for admin.py and models.py

## STEP 4:
Execute Django admin and create details for 10 books

# PROGRAM
models.py
```
from django.db import models
from django.contrib import admin
class book(models.Model):
    Name=models.CharField(max_length=100)
    Book_name=models.CharField(max_length=100)
    Book_code=models.IntegerField()
    Phone_Number=models.CharField(max_length=100)
    Address=models.CharField(max_length=100)
    MRP=models.IntegerField()
class bookadmin(admin.ModelAdmin):
    list_display=("Name","Book_name","Book_code","Phone_Number","Address","MRP")
```
admin.py
```
from django.contrib import admin
from .models import book,bookadmin
admin.site.register(book,bookadmin)
```
# OUTPUT
![Alt text](<../Screenshot 2025-04-15 112730.png>)

# RESULT
Thus the program for creating a database using ORM hass been executed successfully
