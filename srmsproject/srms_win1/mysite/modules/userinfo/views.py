# coding=utf-8

import traceback
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.cache import never_cache
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth import authenticate, login, logout
from django.utils.http import is_safe_url
from django.shortcuts import resolve_url
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.template.response import TemplateResponse
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from mysite import settings
import datetime


class UserinfoList(ListView):
    context_object_name = "userinfo_list"
    template_name = "userinfo_list.html"
    allow_empty = True
    paginate_by = 10

    def get_queryset(self):
        return User.objects.all()


class UserinfoCreate(SuccessMessageMixin, CreateView):
    template_name = "userinfo_edit.html"
    success_url = "/userinfo/list"
    model = User
    fields = ["username", "password", "is_superuser", "is_staff", "email", "gender", "mobile_phone", "photo", "remark1",
              "remark2"]
    success_message = u"%(username)s 成功创建"


    def get_context_data(self, **kwargs):
        context = super(UserinfoCreate, self).get_context_data(**kwargs)
        context["form_content"] = u"新增用户"
        return context

    # 对新增用户密码做加密处理
    def form_valid(self, form):
        form.instance.password = make_password(form.instance.password)
        return super(UserinfoCreate, self).form_valid(form)


class UserinfoUpdate(SuccessMessageMixin, UpdateView):
    template_name = "userinfo_edit.html"
    success_url = "/userinfo/list"
    model = User
    fields = ["username", "password", "is_superuser", "is_staff", "email", "gender", "mobile_phone", "photo", "remark1",
              "remark2"]
    success_message = u"%(username)s 修改成功"

    def get_object(self):
        object = super(UserinfoUpdate, self).get_object()
        return object

    def get_context_data(self, **kwargs):
        context = super(UserinfoUpdate, self).get_context_data(**kwargs)
        context["form_content"] = u"编辑用户信息"
        return context

    # 对编辑用户密码做加密处理
    def form_valid(self, form):
        if form.instance.password != self.get_object().password:
            form.instance.password = make_password(form.instance.password)
        return super(UserinfoUpdate, self).form_valid(form)


class UserinfoDelete(SuccessMessageMixin, DeleteView):
    template_name = "base/confirm_delete.html"
    success_url = "/userinfo/list"
    model = User
    fields = "__all__"
    success_message = u"%(name)s 删除成功"


class UserinfoLogin(View):
    username, password = "", ""

    def get(self, request, *args, **kwargs):
        try:
            template_name = "login.html"
            return render_to_response(template_name, {})
        except:
            traceback.print_exc()

    def post(self, request, *args, **kwargs):
        remember_me = request.POST.get('remember_me', 0)
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        redirect_to = settings.LOGIN_REDIRECT_URL
        user = authenticate(username=username, password=password)
        print "login user==", user
        if user:
            print "is_staff==", user.is_staff
            print "is_active==", user.is_active
        if user and user.is_staff and user.is_active:
            # 确保用户始发重定向的网址是安全的。.
            if not is_safe_url(url=redirect_to, host=request.get_host()):
                redirect_to = resolve_url(settings.LOGIN_REDIRECT_URL)
            # Okay, 安全检查完成，登录用户。
            else:
                login(request, user)
                # 检查是否保存
                if not remember_me:  # 默认14天后登陆超时
                    expiry_time = 1 * 24 * 3600  # 24小时后登陆超时
                    request.session.set_expiry(expiry_time)

            return HttpResponseRedirect(redirect_to)
        elif user and not user.is_staff:
            messages.warning(request, u"您没有登录权限")
        elif user and not user.is_active:
            messages.warning(request, u"您已经离职，无登录权限")
        else:
            messages.warning(request, u"用户名或密码不正确")


class UserinfoLogout(View):
    def get(self, request, *args, **kwargs):
        try:
            template_name = "login.html"
            return render_to_response(template_name, {})
        except:
            traceback.print_exc()
            return redirect(reverse('userinfo:userinfo_login'))

    def post(self, request, *args, **kwargs):
        try:
            return HttpResponse({})
        except:
            traceback.print_exc()


@sensitive_post_parameters()
@csrf_protect
@never_cache
def user_login(request, template_name='login.html', redirect_field_name=REDIRECT_FIELD_NAME,current_app=None):
    """显示登录表单和处理登录动作
    :param request:请求对象
    :param template_name:返回模板的名字
    :param redirect_field_name:重定向字段名
    :param current_app:当前应用程序
    :return:
    """

    redirect_to = request.GET.get(redirect_field_name, "/userinfo/list")
    remember_me = request.POST.get('remember_me', 0)
    username, password = "", ""

    if request.user.is_authenticated:
        return HttpResponseRedirect(redirect_to)

    now = datetime.datetime.now()
    closedate = datetime.datetime(int(settings.CLOSE_DATE[0:4]), int(settings.CLOSE_DATE[4:6]),
                                  int(settings.CLOSE_DATE[6:8]))
    if closedate < now:
        messages.warning(request, u"系统已经超过授权使用时间！")
        return TemplateResponse(request, template_name, {})

    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")

        user = authenticate(username=username, password=password)
        print "login user==", user
        if user:
            print "is_staff==", user.is_staff
            print "is_active==", user.is_active
        if user and user.is_staff and user.is_active:
            # 确保用户始发重定向的网址是安全的。.
            if not is_safe_url(url=redirect_to, host=request.get_host()):
                redirect_to = resolve_url(settings.LOGIN_REDIRECT_URL)
                # return HttpResponse('userinfo_list.html')
            # Okay, 安全检查完成，登录用户。
            else:
                login(request, user)
                # 检查是否保存
                # if not remember_me:  # 默认14天后登陆超时
                #     expiry_time = 1 * 24 * 3600  # 24小时后登陆超时
                #     request.session.set_expiry(expiry_time)

            return HttpResponseRedirect(redirect_to)
        # elif user and not user.is_staff:
        #     login(request, user)
        #     return HttpResponseRedirect("/contentinfo/user/")
        #     # messages.warning(request, u"您没有登录权限")
        elif user and not user.is_active:
            messages.warning(request, u"您已经离职，无登录权限")
        else:
            messages.warning(request, u"用户名或密码不正确")

    current_site = get_current_site(request)

    context = {
        redirect_field_name: redirect_to,
        'site': current_site,
        'site_name': current_site.name,
        "username": username,
        "password": password,
    }

    if current_app:
        request.current_app = current_app
    return TemplateResponse(request, template_name, context)
    # return HttpResponseRedirect("userinfo_list.html")

def user_logout(request):
    def go_back():
        redirect_to = "/userinfo/login"
        return HttpResponseRedirect(redirect_to)

    logout(request)
    return go_back()


class UserinfoHomepage(View):
    def get(self, request, *args, **kwargs):
        try:
            template_name = "homepage.html"
            return render_to_response(template_name, {"request": request})
        except:
            traceback.print_exc()
            return redirect(reverse('userinfo:userinfo_list'))

    def post(self, request, *args, **kwargs):
        try:
            return HttpResponse({})
        except:
            traceback.print_exc()
