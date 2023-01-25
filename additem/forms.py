from django import forms
from app.models import PR, PrItem

class PRForm(forms.ModelForm):
    class Meta:
        model = PR
        fields = ['pr_id', 'submitted_by', 'approval_status', 'marked_by', 'manager_remark', 'date_created']


class PR_ItemForm(forms.ModelForm):
    class Meta:
        model = PrItem
        fields = ['pr_item_id', 'pr_id', 'pr_item_name', 'pr_item_qty', 'pr_item_description']

