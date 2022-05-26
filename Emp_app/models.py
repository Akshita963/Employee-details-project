from django.db import models
import datetime

# Create your models here.
class Employee(models.Model):

    empID = models.AutoField(primary_key=True)
    empName = models.CharField(max_length=100 , blank=False)
    # empDOJ = models.DateField(default=datetime.date.today())
    empDescription = models.CharField(max_length=250,blank=False)
    empCategory = models.CharField(max_length=100,blank=False)
    empCity = models.CharField(max_length=50,blank=False)

    def __str__(self):
        return self.empName
