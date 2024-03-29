"""purchase-requisition-system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from app import views as main_views
from viewItem import views as viewItemview
import django.contrib.auth.views
from django.contrib.auth.views import LoginView, LogoutView
from datetime import datetime

from additem import views as additem_views

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', main_views.home, name='home'),
    re_path(r'^contact$', main_views.contact, name='contact'),
    re_path(r'^about$', main_views.about, name='about'),
    re_path(r'^login/$',
            LoginView.as_view(template_name='app/login.html'),
            name='login'),
    re_path(r'^logout$',
            LogoutView.as_view(template_name='app/index.html'),
            name='logout'),
    re_path(r'^dashboard$', main_views.dashboard, name='dashboard'),

    # addItem views
    path('createpr/', additem_views.create_pr, name='create_pr'),
    path('create_quotation/<str:pr_id>/',
         additem_views.create_quotation, name='create_quotation'),
    path('create_po/<str:quotation_id>/',
         additem_views.create_po, name='create_po'),


    # viewsItem views
    # manager views
    re_path(r'^managerviewpr$', viewItemview.managerviewpr, name='managerviewpr'),
    path('prdetails/<str:pr_id>/', viewItemview.managerviewprdetails,
         name='managerviewprdetails'),
    path('manager_approve_pr', viewItemview.manager_approve_pr,
         name='manager_approve_pr'),
    path('prdetails_approve/<str:pr_id>/',
         viewItemview.manager_approve_pr_details, name='manager_approve_pr_details'),
    re_path(r'^managerviewpo$', viewItemview.managerviewpo, name='managerviewpo'),
    path('managerviewpodetails/<po_id>/',
         viewItemview.managerviewpodetails, name='managerviewpodetails'),


    # update the PR
    path('update_PR/', viewItemview.update_PR, name='update_PR'),

    # employee views
    re_path(r'^employeeviewprhistory$',
            viewItemview.employeeviewprhistory, name='employeeviewprhistory'),
    path('employeeviewprdetails/<str:pr_id>/',
         viewItemview.employeeviewprdetails, name='employeeviewprdetails'),


    # vendor views
    re_path(r'^vendorviewpr$', viewItemview.vendorviewpr, name='vendorviewpr'),
    path('vendorviewprdetails/<str:pr_id>/',
         viewItemview.vendorviewprdetails, name='vendorviewprdetails'),
    re_path(r'^vendorviewqhistory$', viewItemview.vendorviewqhistory,
            name='vendorviewqhistory'),
    path('vendorviewqdetails/<str:quotation_id>/',
         viewItemview.vendorviewqdetails, name='vendorviewqdetails'),



    # purchaser URLs
    re_path(r'^purchaserviewpr$', viewItemview.purchaserviewpr,
            name='purchaserviewpr'),
    path('purchaserviewprdetails/<str:pr_id>/',
         viewItemview.purchaserviewprdetails, name='purchaserviewprdetails'),
    re_path(r'^purchaserviewq$', viewItemview.purchaserviewq,
            name='purchaserviewq'),
    path('purchaserviewqdetails/<str:quotation_id>/',
         viewItemview.purchaserviewqdetails, name='purchaserviewqdetails'),
    path('purchaserapproveq', viewItemview.purchaserapproveq,
         name='purchaserapproveq'),
    path('purchaserapproveqdetails/<quotation_id>',
         viewItemview.purchaserapproveqdetails, name='purchaserapproveqdetails'),
    # update
    path('update_quotation/', viewItemview.update_quotation,
         name='update_quotation'),

    # financeofficer URLs
    re_path(r'^financeofficerviewpr$',
            viewItemview.financeofficerviewpr, name='financeofficerviewpr'),
    path('financeofficerviewprdetails/<str:pr_id>/',
         viewItemview.financeofficerviewprdetails, name='financeofficerviewprdetails'),
    re_path(r'^financeofficerviewq$', viewItemview.financeofficerviewq,
            name='financeofficerviewq'),
    path('financeofficerviewqdetails/<str:quotation_id>/',
         viewItemview.financeofficerviewqdetails, name='financeofficerviewqdetails'),
    re_path(r'^financeofficerviewpohistory$',
            viewItemview.financeofficerviewpohistory, name='financeofficerviewpohistory'),
    path('financeofficerviewpodetails/<po_id>/',
         viewItemview.financeofficerviewpodetails, name='financeofficerviewpodetails'),

]
