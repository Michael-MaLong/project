# coding=utf-8

import json
import traceback
import datetime
from django.utils import timezone
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from modules.contentinfo.models import Contentinfo
from modules.serverinfo.models import ContentSetinfo
from django.contrib.auth.models import User
from modules.serverinfo.models import Serverinfo
from modules.serverinfo.models import ContentSetinfo
from modules.userlog.models import Userlog
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


class ServerinfoInit(LoginRequiredMixin, View):
    context_object_name = "serverinfo_list"
    template_name = "serverinfo_list.html"
    allow_empty = True
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        login_user = self.request.user
        servers = Serverinfo.objects.filter(**kwargs)
        try:
            if servers:
                servers[0].initContent()
                Userlog(User=login_user, opmodel=Serverinfo.__name__, opaction="initContent", opobject=servers[0].id,
                        writetime=datetime.datetime.now()).save()
                servers[0].synctime = datetime.datetime.now()
                servers[0].save()
            messages.add_message(request, messages.SUCCESS, "初始化成功！")
            return redirect(reverse('serverinfo:serverinfo_list'))
        except:
            traceback.print_exc()


class ServerinfoInitPath(LoginRequiredMixin, View):
    context_object_name = "serverinfo_list"
    template_name = "serverinfo_list.html"
    allow_empty = True
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        login_user = self.request.user
        remotepath = "/home/" + login_user
        servers = Serverinfo.objects.filter(**kwargs)
        try:
            if servers:
                servers[0].initPathContent(remotepath)
                Userlog(User=login_user, opmodel=Serverinfo.__name__, opaction="ServerinfoInitPath",
                        opobject=servers[0].id,
                        writetime=datetime.datetime.now()).save()
            messages.add_message(request, messages.SUCCESS, "初始化成功！")
            return redirect(reverse('serverinfo:serverinfo_list'))
        except:
            traceback.print_exc()


class ServerinfoList(LoginRequiredMixin, ListView):
    context_object_name = "serverinfo_list"
    template_name = "serverinfo_list.html"
    allow_empty = True
    paginate_by = 10

    def get_queryset(self):
        return Serverinfo.objects.all()


class ServerinfoCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = "serverinfo_edit.html"
    success_url = "/serverinfo/list"
    model = Serverinfo
    fields = ["name", "ip", "port", "username", "password", "checkflag"]
    success_message = u"%(name)s 成功创建"

    def form_valid(self, form):
        try:
            name = self.request.POST.get("name", "")
            ip = self.request.POST.get("ip", "")
            port = self.request.POST.get("port", "")
            username = self.request.POST.get("username", "")
            password = self.request.POST.get("password", "")

            form.instance.name = name
            form.instance.ip = ip
            form.instance.port = port
            form.instance.username = username
            form.instance.password = password
            form.instance.writetime = datetime.datetime.now()
            return super(ServerinfoCreate, self).form_valid(form)
        except:
            traceback.print_exc()


class ServerinfoUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = "serverinfo_edit.html"
    success_url = "/serverinfo/list"
    model = Serverinfo
    fields = ["name", "ip", "port", "username", "password", "checkflag"]
    success_message = u"%(name)s 修改成功"


    def get_context_data(self, **kwargs):
        context = super(ServerinfoUpdate, self).get_context_data(**kwargs)
        context["form_content"] = u"编辑服务器信息"
        return context

    def form_valid(self, form):
        form.instance.writetime = datetime.datetime.now()
        return super(ServerinfoUpdate, self).form_valid(form)


class ServerinfoDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    template_name = "base/confirm_delete.html"
    success_url = "/serverinfo/list"
    model = Serverinfo
    fields = "__all__"
    success_message = u"%(name)s 删除成功"


class ServerinfoChart(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):

        try:
            template_name = "serverinfo_chart.html"
            all_serverinfo_list = Serverinfo.objects.all()
            results = {"serverlist": all_serverinfo_list}
            return render_to_response(template_name, results)
        except:
            traceback.print_exc()


class ServerinfoSyncContent(LoginRequiredMixin, View):
    context_object_name = "serverinfo_list"
    template_name = "serverinfo_list.html"
    allow_empty = True
    paginate_by = 10
    success_message = u"同步成功"

    def get(self, request, *args, **kwargs):
        login_user = self.request.user
        remotepath = "/home/assets"
        servers = Serverinfo.objects.filter(**kwargs)
        print servers
        try:
            if servers:
                server = servers[0]
                try:
                    conset = ContentSetinfo.objects.get(serverid=server)
                except:
                    conset = None
                if conset:
                    server.syncContent(conset.absname)
                    Userlog(User=login_user, opmodel=Serverinfo.__name__, opaction="syncContent", opobject=server.id,
                            writetime=datetime.datetime.now()).save()
                    messages.add_message(request, messages.SUCCESS, "同步成功！")
                    server.synctime = datetime.datetime.now()
                    server.save()
                else:
                    messages.add_message(request, messages.ERROR, "首先确认配置服务器同步目录！")
            else:
                messages.add_message(request, messages.ERROR, "服务器连接错误，同步失败！")

            return redirect(reverse('serverinfo:serverinfo_list'))
        except:
            traceback.print_exc()


class ServerinfoConn(LoginRequiredMixin, View):
    context_object_name = "serverinfo_list"
    template_name = "serverinfo_list.html"
    allow_empty = True
    paginate_by = 10
    success_message = u"连接成功"

    def get(self, request, *args, **kwargs):
        login_user = self.request.user
        servers = Serverinfo.objects.filter(**kwargs)
        try:
            if servers:
                conn = servers[0].connect()
                Userlog(User=login_user, opmodel=Serverinfo.__name__, opaction="ServerinfoConn", opobject=servers[0].id,
                        writetime=datetime.datetime.now()).save()
                if conn:
                    messages.add_message(request, messages.SUCCESS, "连接成功！")
                else:
                    messages.add_message(request, messages.ERROR, "连接失败！")
            else:
                messages.add_message(request, messages.ERROR, "连接失败！")

            return redirect(reverse('serverinfo:serverinfo_list'))
        except :
            traceback.print_exc()


class ContentSetList(LoginRequiredMixin, ListView):
    context_object_name = "contentset_list"
    template_name = "contentset_list.html"
    allow_empty = True
    paginate_by = 10

    def get_queryset(self):
        return ContentSetinfo.objects.all()


class ContentSetCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = "contentset_edit.html"
    success_url = "/serverinfo/contentset/list"
    model = ContentSetinfo
    fields = "__all__"
    success_message = u"成功创建"

    def form_valid(self, form):
        try:
            serverid = self.request.POST.get("serverid", "")
            absname = self.request.POST.get("absname", "")
            userid = self.request.POST.get("user", "")
            writetime = self.request.POST.get("writetime", "")
            server = Serverinfo.objects.get(id=serverid)
            user = User.objects.get(id=userid)

            form.instance.serverid = server
            form.instance.User = user
            form.instance.absname = absname
            # form.instance.writetime = timezone.now

            return super(ContentSetCreate, self).form_valid(form)
        except:
            traceback.print_exc()


class ContentSetUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = "contentset_edit.html"
    success_url = "/serverinfo/contentset/list"
    model = ContentSetinfo
    fields = ["serverid", "absname", "user"]
    success_message = u" 修改成功"

    def get_context_data(self, **kwargs):
        context = super(ContentSetUpdate, self).get_context_data(**kwargs)
        context["form_content"] = u"编辑配置信息"
        return context


class ContentSetDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    template_name = "base/confirm_delete.html"
    success_url = "/serverinfo/contentset/list"
    model = ContentSetinfo
    fields = "__all__"
    success_message = u"%(name)s 删除成功"
