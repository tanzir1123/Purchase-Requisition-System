from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

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