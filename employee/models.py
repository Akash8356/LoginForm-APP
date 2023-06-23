from django.db import models

# Create your models here.

class Employee(models.Model):
    employee_id = models.TextField(primary_key=True)
    name=models.CharField(max_length=50)
    phone= models.CharField(max_length=10)
    position=models.CharField(max_length=20)
    location =models.CharField(max_length=50)
    about= models.TextField()
    def __str__(self) -> str:
        return self.name+' '+self.phone

