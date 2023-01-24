"""
Definition of models.
"""

from django.db import models

from django.contrib.auth.models import User

#sharing entity

class Item(models.Model):
    item_id = models.CharField(primary_key=True, max_length=10)
    item_name = models.TextField()
    item_description = models.TextField(null=True,default=None, blank=True)
    def __str__(self):
        return str(self.item_id)

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=40, null = True)
    employee_contact = models.CharField(max_length=15, null = True, blank = True)
    def __str__(self):
        return f"{self.employee_id} {self.employee_name}"

class Manager(models.Model):
    manager_id = models.AutoField(primary_key=True)
    manager_name = models.CharField(max_length=40, null=True)
    manager_contact = models.CharField(max_length=15, null= True, blank = True)
    def __str__(self):
        return str(self.manager_id)

class Vendor(models.Model):
    vendor_id = models.AutoField(primary_key=True)
    vendor_name = models.CharField(max_length=40, null=True)
    vendor_contact = models.CharField(max_length=15, null= True, default=True, blank = True)
    vendor_address = models.CharField(max_length=100, null= True, blank = True)
    def __str__(self):
        return str(self.vendor_id)

class Purchaser(models.Model):
    purchaser_id = models.AutoField(primary_key=True)
    purchaser_name = models.CharField(max_length=40, null=True)
    purchaser_contact = models.CharField(max_length=15, null= True, blank = True)
    def __str__(self):
        return str(self.purchaser_id)

class FinanceOfficer(models.Model):
    financeofficer_id = models.AutoField(primary_key=True)
    financeofficer_name = models.CharField(max_length=40, null=True)
    financeofficer_contact = models.CharField(max_length=15, null= True, blank = True)
    def __str__(self):
        return str(self.financeofficer_id)

class PR(models.Model):
    pr_id = models.AutoField(primary_key=True)
    #even after deletion of the Employee, PR record would still be in the database.
    submitted_by = models.ForeignKey(Employee, default=None, on_delete=models.SET_NULL, null=True)
    APPROVAL_STATUS_CHOICES = [
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
        ('Pending', 'Pending'),
    ]
    approval_status = models.CharField(max_length=20, choices = APPROVAL_STATUS_CHOICES, default='Pending')
    marked_by = models.ForeignKey(Manager, default= None, on_delete=models.SET_NULL, null=True)
    manager_remark = models.CharField(max_length=200,null=True)
    date_created = models.DateField()
    def __str__(self):
        return str(self.pr_id)

class PrItem(models.Model):
    pr_item_id = models.AutoField(primary_key=True)
    pr_id = models.ForeignKey(PR, on_delete=models.CASCADE)
    pr_item_name = models.CharField(max_length=40, null=True)
    pr_item_qty = models.PositiveIntegerField(default=None, null=True)
    pr_item_price = models.FloatField(default=None, null=True)
    pr_item_description = models.CharField(max_length=100, default=None, null=True)
    def __str__(self):
        return str(self.ppr_item_id)
