from django import forms
from app.models import PR, PrItem, Quotation, QuotationItem, Purchaseorder

class PRForm(forms.ModelForm):
    class Meta:
        model = PR
        fields = ['pr_id', 'submitted_by', 'approval_status', 'marked_by', 'manager_remark', 'date_created']


class PR_ItemForm(forms.ModelForm):
    class Meta:
        model = PrItem
        fields = ['pr_item_id', 'pr_id', 'pr_item_name', 'pr_item_qty', 'pr_item_description']

class QuotationForm(forms.ModelForm):
    class Meta:
        model = Quotation
        fields = ['quotation_id', 'pr_id', 'vendor_id', 'approval_status', 'checked_by', 'total_price', 'purchaser_remark', 'date_of_expiry', 'q_payment_terms']

class Quotation_ItemForm(forms.ModelForm):
    class Meta:
        model = QuotationItem
        fields = ['q_item_id', 'quotation_id', 'q_item_name', 'q_item_unit_price', 'q_item_qty', 'q_item_price']

class POForm(forms.ModelForm):
    class Meta:
        model = Purchaseorder
        fields = ['po_id', 'financeOfficerId', 'pr_id', 'quotation_id', 'total_price', 'date_created',  'po_terms']
