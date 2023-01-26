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
    pr_list = PR.objects.filter(approval_status__in=['Pending']).values()
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

        print(status_type +" "+ remark)

        if status_type == 'Approved':
            PR.objects.filter(pr_id=pr_id).update(approval_status=status_type)
            PR.objects.filter(pr_id=pr_id).update(manager_remark=remark)
        elif status_type == 'Rejected':
            PR.objects.filter(pr_id=pr_id).update(approval_status=status_type)
            PR.objects.filter(pr_id=pr_id).update(manager_remark=remark)
        return JsonResponse("Status saved", safe=False)
    else:
        return HttpResponseBadRequest("Invalid request method")

@login_required
def vendorviewpr(request):
    pr_list = PR.objects.filter(approval_status__in=['Approved']).values()
    context = {'pr_list': pr_list}
    return render(request, 'vendor/vendorviewpr.html', context)

def vendorviewprdetails(request, pr_id):
    pr = PR.objects.get(pr_id=pr_id)
    pr_items = PrItem.objects.filter(pr_id=pr_id)
    context = {'pr': pr, 'pr_items': pr_items}
    return render(request, 'vendor/vendorviewprdetails.html', context)

@login_required
def employeeviewprhistory(request):
    user_id = Employee.objects.get(user=request.user).employee_id
    pr_list = PR.objects.filter(submitted_by=user_id).values()
    context = {'pr_list': pr_list}
    return render(request, 'employee/employeeviewprhistory.html', context)

def employeeviewprdetails(request, pr_id):
    pr = PR.objects.get(pr_id=pr_id)
    pr_items = PrItem.objects.filter(pr_id=pr_id)
    context = {'pr': pr, 'pr_items': pr_items}
    return render(request, 'employee/employeeviewprdetails.html', context)