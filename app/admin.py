from django.contrib import admin
from app.models import *


# to Display Employee table with the id and the name.
# class EmployeeAdmin(admin.ModelAdmin):
#     list_display = ("employee_id", "employee_name")

admin.site.register(Employee)

# class ManagerAdmin(admin.ModelAdmin):
#     list_display = ("manager_id", "manager_name")

admin.site.register(Manager)

# class VendorAdmin(admin.ModelAdmin):
#     list_display = ("vendor_id", "vendor_name")

admin.site.register(Vendor)

# class PurchaserAdmin(admin.ModelAdmin):
#     list_display = ("purchaser_id", "purchaser_name")

admin.site.register(Purchaser)

# class FinanceofficerAdmin(admin.ModelAdmin):
#     list_display = ("financeofficer_id", "financeofficer_name")

admin.site.register(Financeofficer)
admin.site.register(PR)
admin.site.register(PrItem)
admin.site.register(Quotation)
admin.site.register(QuotationItem)
admin.site.register(Purchaseorder)
admin.site.register(POItem)
