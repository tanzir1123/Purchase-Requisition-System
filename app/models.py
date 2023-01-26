"""
Definition of models.
"""

from django.db import models

from django.contrib.auth.models import User

# sharing entity


class Item(models.Model):
    item_id = models.CharField(primary_key=True, max_length=15)
    item_name = models.TextField()
    item_description = models.TextField(null=True, default=None, blank=True)

    def __str__(self):
        return str(self.item_id)


class Employee(models.Model):
    employee_id = models.CharField(primary_key=True, max_length=15)
    employee_name = models.CharField(max_length=40, null=True)
    employee_contact = models.CharField(max_length=15, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    # Saving with the prefix in the database.
    def save(self, *args, **kwargs):
        if not self.employee_id.startswith('E'):
            self.employee_id = 'E' + self.employee_id
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.employee_id)


class Manager(models.Model):
    manager_id = models.CharField(primary_key=True, max_length=15)
    manager_contact = models.CharField(max_length=15, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    # Saving with the prefix in the database.
    def save(self, *args, **kwargs):
        if not self.manager_id.startswith('M'):
            self.manager_id = 'M' + self.manager_id
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.manager_id)


class Vendor(models.Model):
    vendor_id = models.CharField(primary_key=True, max_length=15)
    vendor_name = models.CharField(max_length=40, null=True)
    vendor_contact = models.CharField(max_length=15, null=True, blank=True)
    vendor_address = models.CharField(max_length=100, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    # Saving with the prefix in the database.
    def save(self, *args, **kwargs):
        if not self.vendor_id.startswith('V'):
            self.vendor_id = 'V' + self.vendor_id
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.vendor_id)


class Purchaser(models.Model):
    purchaser_id = models.CharField(primary_key=True, max_length=15)
    purchaser_name = models.CharField(max_length=40, null=True)
    purchaser_contact = models.CharField(max_length=15, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    # Saving with the prefix in the database.
    def save(self, *args, **kwargs):
        if not self.purchaser_id.startswith('P'):
            self.purchaser_id = 'P' + self.purchaser_id
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.purchaser_id)


class Financeofficer(models.Model):
    financeofficer_id = models.CharField(primary_key=True, max_length=15)
    financeofficer_name = models.CharField(max_length=40, null=True)
    financeofficer_contact = models.CharField(
        max_length=15, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    # Saving with the prefix in the database.
    def save(self, *args, **kwargs):
        if not self.financeofficer_id.startswith('F'):
            self.financeofficer_id = 'F' + self.financeofficer_id
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.financeofficer_id)


class PR(models.Model):
    pr_id = models.CharField(primary_key=True, max_length=15)
    # even after deletion of the Employee, PR record would still be in the database.
    submitted_by = models.ForeignKey(
        Employee, default=None, on_delete=models.SET_NULL, null=True)
    APPROVAL_STATUS_CHOICES = [
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
        ('Pending', 'Pending'),
    ]
    approval_status = models.CharField(
        max_length=20, choices=APPROVAL_STATUS_CHOICES, default='Pending')
    marked_by = models.ForeignKey(
        Manager, default=None, on_delete=models.SET_NULL, null=True, blank=True)
    manager_remark = models.CharField(
        max_length=200, default=None, null=True, blank=True)
    date_created = models.DateField()

    # Saving with the prefix in the database.
    def save(self, *args, **kwargs):
        if not self.pr_id.startswith('PR'):
            self.pr_id = 'PR' + self.pr_id
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.pr_id)


class PrItem(models.Model):
    pr_item_id = models.AutoField(primary_key=True)
    pr_id = models.ForeignKey(PR, on_delete=models.CASCADE)
    pr_item_name = models.CharField(max_length=40, null=True)
    pr_item_qty = models.PositiveIntegerField(default=None, null=True)
    pr_item_description = models.CharField(
        max_length=100, default=None, null=True, blank=True)

    # # Saving with the prefix in the database.
    # def save(self, *args, **kwargs):
    #     if not self.pr_item_id.startswith('PRItem'):
    #         self.pr_item_id = 'PRItem' + self.pr_item_id
    #     super().save(*args, **kwargs)

    def __str__(self):
        return str(self.pr_item_id)


class Quotation(models.Model):
    quotation_id = models.CharField(primary_key=True, max_length=15)
    pr_id = models.ForeignKey(PR, on_delete=models.CASCADE)
    vendor_id = models.ForeignKey(
        Vendor, default=None, on_delete=models.PROTECT, null=True, blank=True)
    APPROVAL_STATUS_CHOICES = [
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
        ('Pending', 'Pending'),
    ]
    approval_status = models.CharField(
        max_length=20, choices=APPROVAL_STATUS_CHOICES, default='Pending')
    checked_by = models.ForeignKey(
        Purchaser, default=None, on_delete=models.SET_NULL, null=True, blank=True)
    total_price = models.FloatField(default=None, null=True)
    purchaser_remark = models.CharField(
        max_length=200, default=None, null=True, blank=True)
    date_of_expiry = models.DateField()
    q_payment_terms = models.CharField(
        max_length=100, default=None, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.quotation_id.startswith('Q'):
            self.quotation_id = 'Q' + self.quotation_id
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.quotation_id)


class QuotationItem(models.Model):
    q_item_id = models.AutoField(primary_key=True)
    quotation_id = models.ForeignKey(Quotation, on_delete=models.CASCADE)
    q_item_name = models.CharField(max_length=20, null=True)
    q_item_unit_price = models.FloatField(default=None, null=True)
    q_item_qty = models.PositiveIntegerField(default=None, null=True)
    q_item_price = models.FloatField(default=None, null=True, blank=True)

    # Saving the Q_Item_Price
    def save(self, *args, **kwargs): 
        self.q_item_price = int(self.q_item_unit_price) * int(self.q_item_qty)
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.q_item_id)


class Purchaseorder(models.Model):
    po_id = models.CharField(primary_key=True, max_length=15)
    financeOfficerId = models.ForeignKey(
        Financeofficer, default=None, on_delete=models.SET_NULL, null=True, blank=True)
    pr_id = models.ForeignKey(PR, on_delete=models.CASCADE)
    quotation_id = models.ForeignKey(Quotation, on_delete=models.CASCADE)
    total_price = models.FloatField(null=True, blank=True)
    date_created = models.DateField()
    po_terms = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.po_id)


class POItem(models.Model):
    po_item_id = models.AutoField(primary_key=True)
    po_id = models.ForeignKey(Purchaseorder, on_delete=models.CASCADE)
    po_item_name = models.CharField(max_length=20, null=True)
    po_unit_price = models.FloatField(default=None, null=True)
    po_item_qty = models.PositiveIntegerField(default=None, null=True)
    po_item_price = models.FloatField(default=None, null=True, blank=True)

    # Saving the PO_Item_Price
    def save(self, *args, **kwargs):
        self.q_item_price = self.po_unit_price * self.po_item_qty
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.po_item_id)
