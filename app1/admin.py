from django.contrib import admin
from.models import Employee
class EmployeAdmin(admin.ModelAdmin):
    list_display=["name","email","password"]
admin.site.register(Employee,EmployeAdmin)

# Register your models here.
