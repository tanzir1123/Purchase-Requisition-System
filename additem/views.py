from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime
# from app.models import Item
from django.shortcuts import render, redirect
from app.models import Employee, QuotationItem, POItem, Quotation
from app.models import PrItem, Vendor, Financeofficer
from .forms import POForm, PRForm, PR_ItemForm, QuotationForm, Quotation_ItemForm
from django.contrib import messages
# Create your views here.


def create_pr(request):
    user_id = Employee.objects.get(user=request.user).employee_id
    context = {'user_id': user_id }

    if request.method == 'POST':
        form = PRForm(request.POST)

        if form.is_valid():
            messages.success(request, 'Data was successfully entered in the database.')
            pr = form.save()
            
            pr_item_name_list = request.POST.getlist('pr_item_name')
            pr_item_quantity_list = request.POST.getlist('pr_item_qty')
            pr_item_description_list = request.POST.getlist('pr_item_description')
            print(pr_item_name_list)
            print(pr)
            print(request.POST.get('number_of_items'))

            # if item_form.is_valid():
            for i in range(int(request.POST.get('number_of_items'))):
                item_obj = PrItem(
                        pr_item_name=pr_item_name_list[i],
                        pr_item_qty=pr_item_quantity_list[i],
                        pr_item_description=pr_item_description_list[i],
                        pr_id=pr
                    )
                item_obj.save()
                print("Successfully created PR")
        else:
            print(form.errors)
            messages.error(request, 'Data was not entered in the database')
            return render(request, 'addItem/create_pr.html', {'form': form})
    
   
    return render(request, 'addItem/create_pr.html', context)

def create_quotation(request, pr_id):
    user_id = Vendor.objects.get(user=request.user).vendor_id
    context = {'user_id': user_id, 'pr_id': pr_id}

    if request.method == 'POST':
        form = QuotationForm(request.POST)

        if form.is_valid():
            messages.success(request, 'Data was successfully entered in the database.')
            q = form.save()
        
            q_item_name_list = request.POST.getlist('q_item_name')
            q_item_unit_price_list = request.POST.getlist('q_item_unit_price')
            q_item_quantity_list = request.POST.getlist('q_item_qty')
    
            print(q_item_name_list)

            print(q)
            print(request.POST.get('number_of_items'))

           
            for i in range(int(request.POST.get('number_of_items'))):
                QuotationItem.objects.create(
                        q_item_name=q_item_name_list[i],
                        q_item_unit_price=q_item_unit_price_list[i],
                        q_item_qty=q_item_quantity_list[i],
                        quotation_id=q
                    )
            
                
                print("Successfully created quotation")
        else:
            print(form.errors)
            messages.error(request, 'Data was not entered in the database')
            return render(request, 'addItem/create_quotation.html', {'form': form})
    
   
    return render(request, 'addItem/create_quotation.html', context)


def create_po(request, quotation_id):
    user_id = Financeofficer.objects.get(user=request.user).financeofficer_id
    pr_id  = Quotation.objects.get(quotation_id=quotation_id).pr_id
    
    context = {'user_id': user_id, 'quotation_id': quotation_id, 'pr_id': pr_id}
    
    if request.method == 'POST':
        form = POForm(request.POST)

        if form.is_valid():
            messages.success(request, 'Data was successfully entered in the database.')
            po = form.save()
        
            po_item_name_list = request.POST.getlist('po_item_name')
            po_item_price_list = request.POST.getlist('po_unit_price')
            po_item_quantity_list = request.POST.getlist('po_item_qty')
    
            print(po_item_name_list)

            print(po)
            print(request.POST.get('number_of_items'))

           
            for i in range(int(request.POST.get('number_of_items'))):
                POItem.objects.create(
                        po_item_name=po_item_name_list[i],
                        po_unit_price=po_item_price_list[i],
                        po_item_qty=po_item_quantity_list[i],
                        po_id=po
                    )
            
                
                print("Successfully PO created!!! ")
        else:
            print(form.errors)
            messages.error(request, 'Data was not entered in the database')
            return render(request, 'addItem/create_po.html', {'form': form})
    
   
    return render(request, 'addItem/create_po.html', context)