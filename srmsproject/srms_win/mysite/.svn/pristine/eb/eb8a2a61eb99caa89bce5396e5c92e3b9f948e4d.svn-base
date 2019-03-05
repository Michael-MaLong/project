# coding=utf-8

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from modules.userlog.models import Userlog
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class UserlogList(LoginRequiredMixin, ListView):
    context_object_name = "userlog_list"
    template_name = "userlog_list.html"
    allow_empty = True
    paginate_by = 10

    def get_queryset(self):
        return Userlog.objects.all()


class UserlogCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = "userlog_edit.html"
    success_url = "/userlog/list"
    model = User
    fields = "__all__"
    success_message = u"%(User.username)s 成功创建"


    def get_context_data(self, **kwargs):
        context = super(UserlogCreate, self).get_context_data(**kwargs)
        context["form_content"] = u"新增日志"
        return context


class UserlogUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = "userlog_edit.html"
    success_url = "/userlog/list"
    model = User
    fields = "__all__"
    success_message = u"%(User.username)s 修改成功"

    def get_context_data(self, **kwargs):
        context = super(UserlogUpdate, self).get_context_data(**kwargs)
        context["form_content"] = u"编辑信息"
        return context


class UserlogDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    template_name = "base/confirm_delete.html"
    success_url = "/userlog/list"
    model = User
    fields = "__all__"
    success_message = u"%(User.username)s 删除成功"
