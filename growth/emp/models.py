from django.db import models

# Create your models here.
class Emp(models.Model):
    emp_no=models.PositiveIntegerField()
    emp_name=models.CharField(max_length=64)
    emp_sal=models.FloatField()