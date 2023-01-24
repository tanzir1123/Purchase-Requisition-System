from django.contrib import admin
from app.models import *

admin.site.register(Item),

# to Display Employee table with the id and the name.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("employee_id", "employee_name")

admin.site.register(Employee, EmployeeAdmin)

class ManagerAdmin(admin.ModelAdmin):
    list_display = ("manager_id", "manager_name")

admin.site.register(Manager, ManagerAdmin)

class VendorAdmin(admin.ModelAdmin):
    list_display = ("vendor_id", "vendor_name")

admin.site.register(Vendor, VendorAdmin)

class PurchaserAdmin(admin.ModelAdmin):
    list_display = ("purchaser_id", "purchaser_name")

admin.site.register(Purchaser, PurchaserAdmin)

class FinanceOfficerAdmin(admin.ModelAdmin):
    list_display = ("financeofficer_id", "financeofficer_name")

admin.site.register(FinanceOfficer, FinanceOfficerAdmin)
admin.site.register(PR)
admin.site.register(PrItem)