# coding=utf-8

from django.conf.urls import url
from modules.serverinfo import views

urlpatterns = [
    url(r'^initpath/', views.ServerinfoInitPath.as_view(), name="serverinfo_initpath"),
    url(r'(?P<pk>[0-9]+)/init', views.ServerinfoInit.as_view(), name="serverinfo_init"),
    url(r'(?P<pk>[0-9]+)/sync/', views.ServerinfoSyncContent.as_view(), name="serverinfo_sync"),
    url(r'(?P<pk>[0-9]+)/conn/', views.ServerinfoConn.as_view(), name="serverinfo_conn"),
    url(r'^list/', views.ServerinfoList.as_view(), name="serverinfo_list"),
    url(r'^add/', views.ServerinfoCreate.as_view(), name="serverinfo_add"),
    url(r'(?P<pk>[0-9]+)/edit$', views.ServerinfoUpdate.as_view(), name="serverinfo_edit"),
    url(r'(?P<pk>[0-9]+)/delete$', views.ServerinfoDelete.as_view(), name="serverinfo_delete"),
    # url(r'^batchdelete/', views.ServerinfoBatchDelete.as_view(), name="serverinfo_batch_delete"),
    url(r'^chart/', views.ServerinfoChart.as_view(), name="serverinfo_chart"),
]
