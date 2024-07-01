from django.contrib import admin
from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    model =  Employee
    list_display = ['id','name','address','phone','email']
    search_fields= ['name']
admin.site.register(Employee, EmployeeAdmin)


# Register your models here.
