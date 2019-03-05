# coding=utf-8

from mysite import settings
import traceback
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
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

from django.shortcuts import render
from modules.common.utils import *
from django.contrib import messages
from django.http import HttpResponse


class SysteminfoInit(LoginRequiredMixin, View):
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


class SysteminfoList(LoginRequiredMixin, ListView):
    context_object_name = "systeminfo_list"
    template_name = "systeminfo_list.html"
    allow_empty = True
    paginate_by = 10

    def get_queryset(self):
        return Systeminfo.objects.all()


class SysteminfoParam(LoginRequiredMixin, ListView):
    context_object_name = "param_list"
    template_name = "systeminfo_param.html"
    allow_empty = True
    paginate_by = 10

    def get_queryset(self):
        return Systeminfo.objects.all()


class SysteminfoCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
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


class SysteminfoUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = "systeminfo_edit.html"
    success_url = "/systeminfo/list"
    model = Systeminfo
    fields = "__all__"
    success_message = u"%(name)s 修改成功"


    def get_context_data(self, **kwargs):
        context = super(SysteminfoUpdate, self).get_context_data(**kwargs)
        context["form_content"] = u"编辑信息"
        return context


class SysteminfoDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    template_name = "base/confirm_delete.html"
    success_url = "/systeminfo/list"
    model = Systeminfo
    fields = "__all__"
    success_message = u"%(name)s 删除成功"


class SystemConfigView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        try:

            import platform
            import uuid


            system = " Microsoft Windows 7"
            mac = "00-50-56-C0-00-08"
            ip = "127.0.0.1"
            cpu = "Intel64 Family 6 Model 2277 Mhz"
            memory = "8.00 GB"
            language = " Python27"
            service = "Apache"
            database = "MySQL"
            nodenumber = "300"
            version = "VERSION 1.0.1"

            system = platform.platform()
            cpu = platform.processor()
            mac = uuid.uuid1().hex[-12:].lower()
            database = settings.DATABASE_ENGINE
            language = settings.LANGUAGE
            nodenumber = settings.NODENUMBER
            version = settings.VERSION

            systeminfo = {"system": system, "mac": mac, "ip": ip, "cpu": cpu, "memory": memory, "language": language,
                          "service": service, "database": database, "nodenumber": nodenumber, "version": version}

            template_name = "systeminfo_config.html"
            return render_to_response(template_name,
                                      {"systeminfo": systeminfo})
        except:
            traceback.print_exc()


class SystemUpdateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        try:
            param_list = Systeminfo.objects.all()
            template_name = "systeminfo_update.html"
            result_dict = {}
            return render(request, template_name, result_dict)
        except:
            traceback.print_exc()

    def post(self, request, *args, **kwargs):
        try:
            template_name = "systeminfo_update.html"
            result_dict = {}

            updatefile = request.POST.get("updatefile", "")
            fs = request.FILES
            if fs.has_key("updatefile"):
                f = fs["updatefile"]
                requestfname = "updatefile"
                fname = "%s%s%s" % (settings.ADDITION_FILE_ROOT, 'upload/system/update/', f)

                uploadfile(request, requestfname, fname)

                updatesys(request)

                messages.add_message(request, messages.SUCCESS, "升级成功！")

            else:
                messages.add_message(request, messages.ERROR, "升级文件不正确，请检查后升级！")

            return render(request, template_name, result_dict)
        except:
            traceback.print_exc()


class SysteminfoParamUpdateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        try:
            param_list = Systeminfo.objects.all()
            template_name = "systeminfo_param.html"
            result_dict = {"param_list": param_list}
            return render(request, template_name, result_dict)
        except:
            traceback.print_exc()

    def post(self, request, *args, **kwargs):
        template_name = "systeminfo_param.html"
        try:
            result_dict = {}
            param_name = request.POST.get("name", "")
            param_value = request.POST.get("newvalue", "")
            try:
                Systeminfo.objects.filter(param_name=param_name).update(param_value=param_value)
                Systeminfo.update_system_cache()
                result_dict["msg"] = "设置成功!"
            except:
                result_dict["msg"] = "设置失败！"

            return HttpResponse(json.dumps(result_dict), content_type="application/json")
        except:
            traceback.print_exc()