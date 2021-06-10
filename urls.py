"""sgs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,re_path
from project.views import supplier_list,user_list,medicine_list,order_list
from project.views import supplier_detail,user_detail,medicine_detail,order_detail
from project.views import medicine_search,medicine_search_all,order_search

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('^api/supplier$',supplier_list),
    re_path('^api/user$',user_list),
    re_path('^api/medicine$',medicine_list),
    re_path('^api/supplier/(?P<pk>[0-9]+)$', supplier_detail),
    re_path('^api/user/(?P<pk>[0-9]+)$', user_detail),
    re_path('^api/medicine/(?P<pk>[0-9]+)$', medicine_detail),
    re_path('^api/order$',order_list),
    re_path('^api/order/(?P<pk>[0-9]+)$', order_detail),
    re_path('^api/medicine/search$',medicine_search),
    re_path('^api/medicine/search/all$',medicine_search_all),
    re_path('^api/order/search$',order_search),
]
