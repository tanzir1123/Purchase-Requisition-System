from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from .models import *


from django.contrib.auth.decorators import login_required


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    if request.user.is_authenticated:
        return (redirect('/menu'))
    else:
        return render(
            request,
            'app/index.html',
            {
                'title': 'Home Page',
                'year': datetime.now().year,
            }
        )


def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title': 'Feel free to reach out at: ',
            'message': 'TANZIR',
            'year': datetime.now().year,
        }
    )


def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'message': 'A Software Engineering project to manage purchase requisitions inside a company (from creating PR, until the generation of a PO). The system involves five actors: Employee, Manager, Vendor, Purchaser, and Finance Officer.',
            'year': datetime.now().year,
        }
    )


@login_required
def dashboard(request):
    is_employee = request.user.groups.filter(name='Employee').exists()
    is_manager = request.user.groups.filter(name='Manager').exists()
    is_vendor = request.user.groups.filter(name='Vendor').exists()
    is_purchaser = request.user.groups.filter(name='Purchaser').exists()
    is_finance_officer = request.user.groups.filter(name='Financeofficer').exists()
    if (is_finance_officer == True):
        print("dEBUGGG: YES IAM THE FINANCE OFFICER\n\n\n")

    if (is_employee == True):
        mydata = Employee.objects.get(user=request.user)
    elif (is_manager == True):
        mydata = Manager.objects.get(user=request.user)
    elif (is_vendor == True):
        mydata = Vendor.objects.get(user=request.user)
    elif (is_purchaser == True):
        mydata = Purchaser.objects.get(user=request.user)
    elif (is_finance_officer == True):
        mydata = Financeofficer.objects.get(
            user=request.user)

    print(mydata)
    context = {
        'mydata': mydata,
        'is_employee': is_employee,
        'is_manager': is_manager,
        'is_vendor': is_vendor,
        'is_purchaser': is_purchaser,
        'is_finance_officer': is_finance_officer
    }
    # context['user'] = request.user

    return render(request, 'app/dashboard.html', context)
