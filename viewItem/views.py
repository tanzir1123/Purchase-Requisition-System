from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from app.models import Manager
from app.models import *


@login_required
def managerviewpr(request):
    pr_list = PR.objects.all()
    context = {'pr_list': pr_list}
    return render(request, 'manager/managerviewpr.html', context)


@login_required
def managerviewprdetails(request, pr_id):
    pr = PR.objects.get(pr_id=pr_id)
    pr_items = PrItem.objects.filter(pr_id=pr_id)
    context = {'pr': pr, 'pr_items': pr_items}
    return render(request, 'manager/prdetails.html', context)


def manager_approve_pr(request):
    pr_list = PR.objects.filter(approval_status__in=['Pending'])
    context = {'pr_list': pr_list}
    return render(request, 'manager/managerapprovepr.html', context)


def manager_approve_pr_details(request, pr_id):
    pr = PR.objects.get(pr_id=pr_id)
    pr_items = PrItem.objects.filter(pr_id=pr_id)

    context = {'pr': pr, 'pr_items': pr_items}
    return render(request, 'manager/prdetails_approve.html', context)

@csrf_exempt
def update_PR(request):
    if request.method == 'POST':
        pr_id = request.POST.get('pr_id')
        status_type = request.POST.get('status_type')
        remark = request.POST.get('remark')
        manager_id = Manager.objects.get(user=request.user).manager_id

        print(status_type + " " + remark)

        if status_type == 'Approved':
            PR.objects.filter(pr_id=pr_id).update(approval_status=status_type)
            PR.objects.filter(pr_id=pr_id).update(manager_remark=remark)
            PR.objects.filter(pr_id=pr_id).update(marked_by=manager_id)
        elif status_type == 'Rejected':
            PR.objects.filter(pr_id=pr_id).update(approval_status=status_type)
            PR.objects.filter(pr_id=pr_id).update(manager_remark=remark)
            PR.objects.filter(pr_id=pr_id).update(marked_by=manager_id)
        return JsonResponse("Status saved", safe=False)
    else:
        return HttpResponseBadRequest("Invalid request method")

@login_required
def managerviewpo(request):
    po_list = Purchaseorder.objects.all()
    context = {'po_list': po_list}
    return render(request, 'manager/managerviewpo.html', context)

def managerviewpodetails(request, po_id):
    po = Purchaseorder.objects.get(po_id=po_id)
    po_items = POItem.objects.filter(po_id=po_id)
    
    context = {'po' : po, 'po_items': po_items}
    return render(request, 'manager/managerviewpodetails.html', context)


@login_required
def vendorviewpr(request):
    pr_list = PR.objects.filter(approval_status__in=['Approved'])
    context = {'pr_list': pr_list}
    return render(request, 'vendor/vendorviewpr.html', context)


def vendorviewprdetails(request, pr_id):
    pr = PR.objects.get(pr_id=pr_id)
    pr_items = PrItem.objects.filter(pr_id=pr_id)
    context = {'pr': pr, 'pr_items': pr_items}
    return render(request, 'vendor/vendorviewprdetails.html', context)

@login_required
def vendorviewqhistory(request):
    user_id = Vendor.objects.get(user=request.user).vendor_id
    q_list = Quotation.objects.filter(vendor_id = user_id)
    context = {'q_list': q_list}
    return render(request, 'vendor/vendorviewqhistory.html', context)

def vendorviewqdetails(request, quotation_id):
    q = Quotation.objects.get(quotation_id=quotation_id)
    q_items = QuotationItem.objects.filter(quotation_id=quotation_id)
    context = {'q' : q, 'q_items': q_items}
    return render(request, 'vendor/vendorviewqdetails.html',context)


@login_required
def employeeviewprhistory(request):
    user_id = Employee.objects.get(user=request.user).employee_id
    pr_list = PR.objects.filter(submitted_by=user_id)
    context = {'pr_list': pr_list}
    return render(request, 'employee/employeeviewprhistory.html', context)


def employeeviewprdetails(request, pr_id):
    pr = PR.objects.get(pr_id=pr_id)
    pr_items = PrItem.objects.filter(pr_id=pr_id)
    context = {'pr': pr, 'pr_items': pr_items}
    return render(request, 'employee/employeeviewprdetails.html', context)


@login_required
def purchaserviewpr(request):
    pr_list = PR.objects.filter(approval_status__in=['Approved'])
    context = {'pr_list': pr_list}
    return render(request, 'purchaser/purchaserviewpr.html', context)


def purchaserviewprdetails(request, pr_id):
    pr = PR.objects.get(pr_id=pr_id)
    pr_items = PrItem.objects.filter(pr_id=pr_id)
    context = {'pr': pr, 'pr_items': pr_items}
    return render(request, 'purchaser/purchaserviewprdetails.html', context)


@login_required
def purchaserviewq(request):
    q_list = Quotation.objects.all()
    context = {'q_list': q_list}
    return render(request, 'purchaser/purchaserviewq.html', context)


def purchaserviewqdetails(request, quotation_id):
    q = Quotation.objects.get(quotation_id=quotation_id)
    q_items = QuotationItem.objects.filter(quotation_id=quotation_id)
    context = {'q' : q, 'q_items': q_items}
    return render(request, 'purchaser/purchaserviewqdetails.html',context)

@login_required
def purchaserapproveq(request):
    q_list = Quotation.objects.filter(approval_status__in=['Pending']).values()
    context = {'q_list': q_list}
    return render(request, 'purchaser/purchaserapproveq.html', context)

def purchaserapproveqdetails(request, quotation_id):
    q = Quotation.objects.get(quotation_id=quotation_id)
    q_items = QuotationItem.objects.filter(quotation_id=quotation_id)
    context = {'q' : q, 'q_items': q_items}
    return render(request, 'purchaser/purchaserapproveqdetails.html', context)
    
@csrf_exempt
def update_quotation(request):
    if request.method == 'POST':
        quotation_id = request.POST.get('quotation_id')
        status_type = request.POST.get('status_type')
        remark = request.POST.get('remark')
        purchaser_id = Purchaser.objects.get(user=request.user).purchaser_id

        print( status_type + " " + remark + '\n\n\n\n')

        if status_type == 'Approved':
            Quotation.objects.filter(quotation_id=quotation_id).update(approval_status=status_type)
            Quotation.objects.filter(quotation_id=quotation_id).update(purchaser_remark=remark)
            Quotation.objects.filter(quotation_id=quotation_id).update(checked_by=purchaser_id)
        elif status_type == 'Rejected':
            Quotation.objects.filter(quotation_id=quotation_id).update(approval_status=status_type)
            Quotation.objects.filter(quotation_id=quotation_id).update(purchaser_remark=remark)
            Quotation.objects.filter(quotation_id=quotation_id).update(checked_by=purchaser_id)
        return JsonResponse("Status saved", safe=False)
    else:
        return HttpResponseBadRequest("Invalid request method")

@login_required
def financeofficerviewpr(request):
    pr_list = PR.objects.filter(approval_status__in=['Approved'])
    context = {'pr_list': pr_list}
    return render(request, 'financeofficer/financeofficerviewpr.html', context)

def financeofficerviewprdetails(request, pr_id):
    pr = PR.objects.get(pr_id=pr_id)
    pr_items = PrItem.objects.filter(pr_id=pr_id)
    context = {'pr': pr, 'pr_items': pr_items}
    return render(request, 'financeofficer/financeofficerviewprdetails.html', context)

@login_required
def financeofficerviewq(request):
    q_list = Quotation.objects.filter(approval_status__in=['Approved'])
    context = {'q_list': q_list}
    return render(request, 'financeofficer/financeofficerviewq.html', context)

def financeofficerviewqdetails(request, quotation_id):
    q = Quotation.objects.get(quotation_id=quotation_id)
    q_items = QuotationItem.objects.filter(quotation_id=quotation_id)
    context = {'q' : q, 'q_items': q_items}
    return render(request, 'financeofficer/financeofficerviewqdetails.html',context)

@login_required
def financeofficerviewpohistory(request):
    user_id = Financeofficer.objects.get(user=request.user).financeofficer_id
    po_list = Purchaseorder.objects.filter(financeOfficerId=user_id)
    context = {'po_list': po_list}
    return render(request, 'financeofficer/financeofficerviewpohistory.html', context)

def financeofficerviewpodetails(request, po_id):
    po = Purchaseorder.objects.get(po_id=po_id)
    po_items = POItem.objects.filter(po_id=po_id)
    
    print(po_items)
    context = {'po' : po, 'po_items': po_items}
    return render(request, 'financeofficer/financeofficerviewpodetails.html', context)

