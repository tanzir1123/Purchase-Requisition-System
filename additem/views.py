from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime
# from app.models import Item
from django.shortcuts import render, redirect
from app.models import Employee
from app.models import PrItem, Vendor
from .forms import PRForm, PR_ItemForm, QuotationForm, Quotation_ItemForm
from django.contrib import messages
# Create your views here.


# def additemform(request):
#     context = {
#         'title': 'Add Item Form',
#         'year': datetime.now().year,
#     }
#     context['user'] = request.user

#     return render(request, 'additem/additemform.html', context)


# def additemconfirmation(request):
#     print(request)

#     newitem_id = request.POST['item_id']
#     newitem_name = request.POST['item_name']
#     newitem_description = request.POST['item_description']

#     newitem = Item(item_id=newitem_id, item_name=newitem_name,
#                    item_description=newitem_description)
#     newitem.save()

#     context = {

#         'item_id': newitem_id,
#         'item_name': newitem_name,
#         'item_description': newitem_description,
#     }
#     return render(request, 'additem/additemconfirmation.html', context)


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
                item_obj = Quotation_ItemForm(
                        q_item_name=q_item_name_list[i],
                        q_item_unit_price=q_item_unit_price_list[i],
                        q_item_qty=q_item_quantity_list[i],
                        quotation_id=q
                    )
                item_obj.save()
                
                print("Successfully created quotation")
        else:
            print(form.errors)
            messages.error(request, 'Data was not entered in the database')
            return render(request, 'addItem/create_quotation.html', {'form': form})
    
   
    return render(request, 'addItem/create_quotation.html', context)
