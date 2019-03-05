# coding=utf-8

from django.conf.urls import url
from modules.systeminfo import views

urlpatterns = [
    url(r'^list/', views.SysteminfoList.as_view(), name="systeminfo_list"),
    url(r'^config/', views.SystemConfigView.as_view(), name="systeminfo_config"),
]
