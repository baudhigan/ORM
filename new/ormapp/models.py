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