# coding=utf-8
import traceback
import json

from django.shortcuts import render_to_response
from django.views.generic import View
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse


def redirect_404_error(request):
    return render_to_response('error/404.html', {})


def redirect_500_error(request):
    return render_to_response('error/500.html', {})


def redirect_403_error(request):
    return render_to_response('error/403.html', {})


def redirect_400_error(request):
    return render_to_response('error/400.html', {})


class IndexView(View):
    def get(self, request, *args, **kwargs):
        template_name = "index.html"
        return render_to_response(template_name, {})


class SidebarMenusList(View):
    def get(self, request, *args, **kwargs):
        try:
            self.user = request.user
            result_menu_list = self.get_menu_list()
            result = json.dumps({"data": result_menu_list})
            return HttpResponse(result, content_type="application/json")
        except:
            traceback.print_exc()

    def get_menu_list(self):
        try:
            menu_list = [
                {'permissions': '', "show": True, "text": "我的主页",
                 "icon": "menu-icon fa fa-tachometer", "url": ""},

                {'permissions': '', "show": True, "text": "系统监控",
                 "icon": "menu-icon fa fa-desktop",
                 "url": "",
                 "menus": [
                     {'permissions': '', "show": True,
                      "text": "监控资源图表", "icon": "", "url": "/contentinfo/chart/"},
                     {'permissions': '', "show": True, "text": "监控资源列表",
                      "icon": "", "url": "/contentinfo/list/"},
                 ]},

                {"permissions": "", "show": True, "text": "用户管理",
                 "icon": "menu-icon fa fa-list", "url": "",
                 "menus": [
                     {"permissions": "", "show": True, "text": "用户信息",
                      "icon": "", "url": "/userinfo/list/"},
                     {"permissions": "", "show": True, "text": "初始化数据",
                      "icon": "", "url": "/contentinfo/init/"},
                     {"permissions": "", "show": True, "text": "初始化路径",
                      "icon": "", "url": "/serverinfo/initpath/"},
                     {"permissions": "", "show": True, "text": "同步数据",
                      "icon": "", "url": "/serverinfo/sync/"},
                     {"permissions": "", "show": True, "text": "操作日志",
                      "icon": "", "url": "/userlog/list/"},

                 ]},

                {'permissions': '', "show": True, "text": "任务配置",
                 "icon": "menu-icon fa fa-tag",
                 "url": "",
                 "menus": [
                     {'permissions': '', "show": True,
                      "text": "主机配置", "icon": "", "url": "/serverinfo/list/"},
                     {'permissions': '', "show": True, "text": "业务配置",
                      "icon": "", "url": ""},
                 ]},

                {'permissions': '', "show": True, "text": "系统配置",
                 "icon": "menu-icon fa fa-cogs",
                 "url": "",
                 "menus": [
                     {'permissions': '', "show": True,
                      "text": "系统参数", "icon": "", "url": "/systeminfo/list/"},
                 ]},

            ]
            if not self.user.is_superuser:
                for one_menu in menu_list:
                    if not self.user.has_perm(one_menu["permissions"]):
                        one_menu["show"] = False
                        if one_menu.has_key("menus"):
                            for sub in one_menu["menus"]:
                                if not self.user.has_perm(sub["permissions"]):
                                    sub["show"] = False

            return menu_list
        except:
            traceback.print_exc()
            return list()