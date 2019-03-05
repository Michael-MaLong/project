# coding=utf-8
"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import include, url
from django.views.static import serve
from django.http import HttpResponseRedirect
from django.contrib import admin

from mysite import settings
from modules.common.views import SidebarMenusList


handler500 = "modules.common.views.redirect_500_error"
handler404 = "modules.common..views.redirect_404_error"
handler403 = "modules.common..views.redirect_403_error"
handler400 = "modules.common..views.redirect_400_error"


def index(request):
    response = HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
    return response


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^', admin.site.urls),
    url(r'^$', index),
    url(r'^homepage/', include('modules.common.urls', namespace='homepage')),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_PATH, }),
    url(r'^contentinfo/', include('modules.contentinfo.urls', namespace='contentinfo')),
    url(r'^serverinfo/', include('modules.serverinfo.urls', namespace='serverinfo')),
    url(r'^userinfo/', include('modules.userinfo.urls', namespace='userinfo')),
    url(r'^userlog/', include('modules.userlog.urls', namespace='userlog')),
    url(r'^systeminfo/', include('modules.systeminfo.urls', namespace='systeminfo')),
    url(r'^getmenubyuser/$', SidebarMenusList.as_view(), name='getmenubyuser'),
]
