from django.contrib import admin
from Emp_app.models import Employee

# Register your models here.
class show(admin.ModelAdmin):
    list_display = ('empID','empName','empDescription','empCategory','empCity')

admin.site.register(Employee)