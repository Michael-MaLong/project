# coding=utf-8

from django.conf.urls import url
from modules.userinfo import views

urlpatterns = [
    url(r'login/$', views.user_login, name='userinfo_login'),
    url(r'logout/$', views.user_logout, name='userinfo_logout'),
    url(r'^stafflist/', views.UserinfoList.as_view(), name="userinfo_list"),
    # url(r'^login/', views.UserinfoLogin.as_view(), name="userinfo_login"),
    # url(r'^logout/', views.UserinfoLogout.as_view(), name="userinfo_logout"),
    url(r'^list/', views.UserinfoList.as_view(), name="userinfo_list"),
    url(r'^add/', views.UserinfoCreate.as_view(), name="userinfo_add"),
    url(r'(?P<pk>[0-9]+)/edit$', views.UserinfoUpdate.as_view(), name="userinfo_edit"),
    # url(r'(?P<pk>[0-9]+)/delete$', views.UserinfoDelete.as_view(), name="userinfo_delete"),
    # url(r'^batchdelete/', views.UserinfoBatchDelete.as_view(), name="userinfo_batch_delete"),
    url(r'^homepage/', views.UserinfoHomepage.as_view(), name="userinfo_homepage"),
]
