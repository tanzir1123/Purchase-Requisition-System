from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from app.models import Manager
from app.models import PR

@login_required
def managerviewpr(request):
    pr_list = PR.objects.all()
    context = {'pr_list': pr_list}
    return render(request, 'manager/managerviewpr.html', context)
