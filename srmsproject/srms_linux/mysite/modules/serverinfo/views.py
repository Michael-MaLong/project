# coding=utf-8

import json
import traceback
import datetime
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from modules.contentinfo.models import Contentinfo

from modules.serverinfo.models import Serverinfo
from modules.userlog.models import Userlog


class ServerinfoInit(View):
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

            return redirect(reverse('serverinfo:serverinfo_list'))
        except:
            traceback.print_exc()


class ServerinfoInitPath(View):
    context_object_name = "serverinfo_list"
    template_name = "serverinfo_list.html"
    allow_empty = True
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        name = "QiaoTest"
        ip = "192.168.174.128"
        port = 22
        username = "redhat"
        password = "redhat"
        remotepath = "/home/redhat/tomcat-8.5.14"
        try:
            server = Serverinfo(name, ip, port, username, password)
            # server.save()
            server.initPathContent(remotepath)
            return redirect(reverse('serverinfo:serverinfo_list'))
        except:
            traceback.print_exc()


class ServerinfoList(ListView):
    context_object_name = "serverinfo_list"
    template_name = "serverinfo_list.html"
    allow_empty = True
    paginate_by = 10

    def get_queryset(self):
        return Serverinfo.objects.all()


class ServerinfoCreate(SuccessMessageMixin, CreateView):
    template_name = "serverinfo_edit.html"
    success_url = "/serverinfo/list"
    model = Serverinfo
    fields = ["name", "ip", "port", "username", "password"]
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
            return super(ServerinfoCreate, self).form_valid(form)
        except:
            traceback.print_exc()


class ServerinfoUpdate(SuccessMessageMixin, UpdateView):
    template_name = "serverinfo_edit.html"
    success_url = "/serverinfo/list"
    model = Serverinfo
    fields = ["name", "ip", "port", "username", "password"]
    success_message = u"%(name)s 修改成功"


    def get_context_data(self, **kwargs):
        context = super(ServerinfoUpdate, self).get_context_data(**kwargs)
        context["form_content"] = u"编辑服务器信息"
        return context


class ServerinfoDelete(SuccessMessageMixin, DeleteView):
    template_name = "base/confirm_delete.html"
    success_url = "/serverinfo/list"
    model = Serverinfo
    fields = "__all__"
    success_message = u"%(name)s 删除成功"


class ServerinfoChart(View):
    def get(self, request, *args, **kwargs):
        try:
            template_name = "serverinfo_chart.html"
            return render_to_response(template_name, {})
        except:
            traceback.print_exc()

    def post(self, request, *args, **kwargs):
        try:
            action = self.request.POST.get("action", "")
            # [{"id": "1", "pid": "0", "name": "aaa", "childrens": []}]，最终返回数据结构

            if action == "org_select":  # 取架构数据
                all_content_list = Serverinfo.objects.values()
                self.result_list = list()  # 最终返回树形列表
                if not all_content_list:
                    default_dict = {"id": "", "name": "无", "pid": "", "childrens": list()}
                    self.result_list.append(default_dict)
                else:
                    for one_dept_dict in all_content_list:
                        dept_id = one_dept_dict["id"]  # 部门id
                        dept_name = one_dept_dict["name"]  # 部门名称
                        parent_id = one_dept_dict["parent_dept"]  # 父部门id

                        # 当前部门信息，父部门id是0，代表没有上级部门，为根跟部门
                        if parent_id == 0:
                            # 创建根部门结构
                            root_dep_dict = {"id": dept_id, "name": dept_name,
                                             "pid": parent_id,
                                             "childrens": list()}
                            self.result_list.append(root_dep_dict)  # 添加到最终返回树形列表
                            continue

                        # 当前部门信息，父部门id不为0，存在上级部门
                        if parent_id != 0:
                            # 为父节点添加子节点
                            new_result_list = self.update_result_list(self.result_list,
                                                                      one_dept_dict)

                            # 当前节点不能作为子节点添加到父节点，创建当前节点为根节点
                            if not new_result_list:  # 没有根节点
                                root_dep_dict = {"id": dept_id, "name": dept_name,
                                                 "pid": parent_id, "childrens": list()}
                                self.result_list.append(root_dep_dict)  # 添加到最终返回树形列表

            results = json.dumps(self.result_list)
            return HttpResponse(results)
        except:
            traceback.print_exc()


class ServerinfoSyncContent(View):
    context_object_name = "serverinfo_list"
    template_name = "serverinfo_list.html"
    allow_empty = True
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        login_user = self.request.user
        remotepath = "/home/redhat"
        servers = Serverinfo.objects.filter(**kwargs)
        try:
            if servers:
                servers[0].syncContent(remotepath)
                Userlog(User=login_user, opmodel=Serverinfo.__name__, opaction="syncContent", opobject=servers[0].id,
                        writetime=datetime.datetime.now()).save()

            return redirect(reverse('serverinfo:serverinfo_list'))
        except:
            traceback.print_exc()


class ServerinfoConn(View):
    context_object_name = "serverinfo_list"
    template_name = "serverinfo_list.html"
    allow_empty = True
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        login_user = self.request.user
        servers = Serverinfo.objects.filter(**kwargs)
        try:
            if servers:
                conn = servers[0].connect()
                Userlog(User=login_user, opmodel=Serverinfo.__name__, opaction="ServerinfoConn", opobject=servers[0].id,
                        writetime=datetime.datetime.now()).save()

            return redirect(reverse('serverinfo:serverinfo_list'))
        except:
            traceback.print_exc()