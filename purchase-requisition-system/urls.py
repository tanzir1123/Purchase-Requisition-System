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
        LoginView.as_view(template_name = 'app/login.html'),
        name='login'),
    re_path(r'^logout$',
        LogoutView.as_view(template_name = 'app/index.html'),
        name='logout'),
    re_path(r'^dashboard$', main_views.dashboard, name='dashboard'),


    # viewsItem views
    # manager views
    re_path(r'^managerviewpr$', viewItemview.managerviewpr, name='managerviewpr'),
    path('prdetails/<str:pr_id>/', viewItemview.managerviewprdetails, name='managerviewprdetails'),
    path('manager_approve_pr', viewItemview.manager_approve_pr, name='manager_approve_pr'),
    path('prdetails_approve/<str:pr_id>/', viewItemview.manager_approve_pr_details, name='manager_approve_pr_details'),
    # update 
    path('update_PR/', viewItemview.update_PR, name='update_PR'),


    # addItem views
    # re_path(r'^additemform$', additem_views.additemform, name='additem_form'),
    # re_path(r'^additemconfirmation$', additem_views.additemconfirmation, name='additem_confirmation'),
    path('createpr/', additem_views.create_pr, name='create_pr')
    # re_path(r'^add_pr_item$', additem_views.add_pr_item, name='add_pr_item')
]
