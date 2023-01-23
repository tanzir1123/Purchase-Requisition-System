from django.contrib import admin
from app.models import *

admin.site.register(Item),

# to Display Employee table with the id and the name.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("employee_id", "employee_name")

admin.site.register(Employee, EmployeeAdmin)