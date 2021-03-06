from django.conf.urls import include, url
from modules.contentinfo import views


urlpatterns = [
    url(r'^init/', views.ContentinfoInit.as_view(), name="contentinfo_init"),
    url(r'^list/', views.ContentinfoList.as_view(), name="contentinfo_list"),
    url(r'^add/', views.ContentinfoCreate.as_view(), name="contentinfo_add"),
    url(r'^edit/', views.ContentinfoList.as_view(), name="contentinfo_edit"),
    url(r'^delete/', views.ContentinfoList.as_view(), name="contentinfo_delete"),
    url(r'^chart/', views.ContentinfoChart.as_view(), name="contentinfo_chart"),
    url(r'^user/', views.ContentinfoUser.as_view(), name="contentinfo_user"),
]
