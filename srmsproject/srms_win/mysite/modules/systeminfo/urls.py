# coding=utf-8

from django.conf.urls import url
from modules.systeminfo import views

urlpatterns = [
    url(r'^param/', views.SysteminfoParam.as_view(), name="systeminfo_param"),
    url(r'^paramupdate/', views.SysteminfoParamUpdateView.as_view(), name="systeminfo_paramupdate"),
    url(r'^list/', views.SysteminfoList.as_view(), name="systeminfo_list"),
    url(r'^config/', views.SystemConfigView.as_view(), name="systeminfo_config"),
    url(r'^update/', views.SystemUpdateView.as_view(), name="systeminfo_update"),
]
