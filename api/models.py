from django.db import models

# Create your models here.

# Creating Company Model
class Company(models.Model):
    Company_id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    location =models.CharField(max_length=50)
    about= models.TextField()
# Creating Employee Model
class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    phone= models.CharField(max_length=10,default=9898989890)
    position=models.CharField(max_length=20,default="xyd")
    location =models.CharField(max_length=50)
    about= models.TextField()

