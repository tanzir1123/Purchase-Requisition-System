from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from .models import Manager

from django.contrib.auth.decorators import login_required

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    if request.user.is_authenticated:
        return(redirect('/menu'))
    else:
        return render(
            request,
            'app/index.html',
            {
                'title':'Home Page',
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
            'title':'Contact',
            'message':'Dr. Yeoh.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'ABC System',
            'message':'This application processes ...',
            'year':datetime.now().year,
        }
    )

@login_required
def dashboard(request):
    
    is_manager = request.user.groups.filter(name='Manager').exists()
    
    # if(is_vendor == True):
    #     mydata = Salesman.objects.get(user=request.user).salesman_id
    # if(is_employee == True):
    #     mydata = Customer.objects.get(user=request.user).customer_id
    if(is_manager == True):
        mydata = Manager.objects.get(user=request.user).manager_id
        print(mydata)
    # if(is_finance_officer == True):
    #     mydata = FinanceOfficer.objects.get(user=request.user).finance_officer_id  
    
    context = {
            'mydata': mydata,
            'is_manager': is_manager
        }
    context['user'] = request.user

    return render(request,'app/dashboard.html',context)