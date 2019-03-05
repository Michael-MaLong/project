from django.conf.urls import include, url
from modules.userlog import views

urlpatterns = [
    url(r'^list/', views.UserlogList.as_view(), name="userlog_list"),
    url(r'^add/', views.UserlogCreate.as_view(), name="userlog_add"),
    url(r'(?P<pk>[0-9]+)/edit$', views.UserlogUpdate.as_view(), name="userlog_edit"),
    # url(r'(?P<pk>[0-9]+)/delete$', views.UserlogDelete.as_view(), name="userlog_delete"),
]
