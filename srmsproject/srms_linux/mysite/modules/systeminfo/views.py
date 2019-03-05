# coding=utf-8

import traceback

from django.shortcuts import render_to_response
from django.apps import AppConfig
from django.template import RequestContext
from django.views.generic import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from modules.systeminfo.models import Systeminfo
from modules.systeminfo import models as system_app


class SysteminfoInit(View):
    context_object_name = "systeminfo_list"
    template_name = "systeminfo_list.html"
    allow_empty = True
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        name = "QiaoTest"
        ip = "192.168.174.128"
        port = 22
        username = "redhat"
        password = "redhat"
        try:
            server = Systeminfo(name, ip, port, username, password)
            server.save()
            # server.initContent()
            return redirect(reverse('systeminfo:systeminfo_list'))
        except:
            traceback.print_exc()


class SysteminfoList(ListView):
    context_object_name = "systeminfo_list"
    template_name = "systeminfo_list.html"
    allow_empty = True
    paginate_by = 10

    def get_queryset(self):
        return Systeminfo.objects.all()


class SysteminfoCreate(SuccessMessageMixin, CreateView):
    template_name = "systeminfo_edit.html"
    success_url = "/systeminfo/list"
    model = Systeminfo
    fields = "__all__"
    success_message = u"%(name)s 成功创建"

    def form_valid(self, form):
        try:
            name = self.request.POST.get("name", "")
            ip = self.request.POST.get("ip", "")
            port = self.request.POST.get("port", "")
            username = self.request.POST.get("username", "")
            password = self.request.POST.get("password", "")
            writetime = self.request.POST.get("writetime", "")

            form.instance.name = name
            form.instance.ip = ip
            form.instance.port = port
            form.instance.username = username
            form.instance.password = password
            form.instance.writetime = writetime
            return super(SysteminfoCreate, self).form_valid(form)
        except:
            traceback.print_exc()


class SysteminfoUpdate(SuccessMessageMixin, UpdateView):
    template_name = "systeminfo_edit.html"
    success_url = "/systeminfo/list"
    model = Systeminfo
    fields = "__all__"
    success_message = u"%(name)s 修改成功"


    def get_context_data(self, **kwargs):
        context = super(SysteminfoUpdate, self).get_context_data(**kwargs)
        context["form_content"] = u"编辑信息"
        return context


class SysteminfoDelete(SuccessMessageMixin, DeleteView):
    template_name = "base/confirm_delete.html"
    success_url = "/systeminfo/list"
    model = Systeminfo
    fields = "__all__"
    success_message = u"%(name)s 删除成功"


class SystemConfigView(View):
    def get(self, request, *args, **kwargs):
        try:
            param_list = Systeminfo.objects.all()
            print Systeminfo.get_param("site_name")
            template_name = "systeminfo_list.html"
            return render_to_response(template_name,
                                      {"param_list": param_list},
                                      context_instance=RequestContext(request))
        except:
            traceback.print_exc()

