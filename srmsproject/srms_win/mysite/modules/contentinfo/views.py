# coding=utf-8

import json
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template import RequestContext
from django.views.generic import View
from django.views.generic import ListView
import datetime
import traceback
import random
from modules.contentinfo.models import Contentinfo
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from modules.serverinfo.models import Serverinfo
from modules.systeminfo.models import Systeminfo

#maybe for mac
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class ContentinfoInit(LoginRequiredMixin, View):
    context_object_name = "contentinfo_list"
    template_name = "contentinfo_list.html"
    allow_empty = True
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        name = "QiaoTest"
        ip = "192.168.174.131"
        port = 22
        username = "redhat"
        password = "redhat"
        try:
            server = Serverinfo(name=name, ip=ip, port=port, username=username, password=password)
            server.save()
            server.initContent()
            return redirect(reverse('contentinfo:contentinfo_list'))
        except:
            traceback.print_exc()


class ContentinfoPathInit(LoginRequiredMixin, View):
    context_object_name = "contentinfo_list"
    template_name = "contentinfo_list.html"
    allow_empty = True
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        server = "192.168.174.128"
        remotepath = "/home/redhat/tomcat-8.5.14"
        try:
            dirlist = remotepath.split("/")
            templist = dirlist[1:]
            count = remotepath.count("/")
            alldir = []
            pwddir = ""
            for l in range(count):
                i = 1
                tempdir = ""
                for i in range(i):
                    tempdir = "/" + templist[l]
                    pwddir += tempdir
                    i += 1
                alldir.append(pwddir)

                content = Contentinfo(name=pwddir, type=1, superid=0, serverid=server, changeflag=0, oldproperty=0,
                                      newproperty=0,
                                      flag=0, writetime='00')
                content.save()

            return redirect(reverse('contentinfo:contentinfo_list'))
        except:
            traceback.print_exc()


class ContentinfoList(LoginRequiredMixin, ListView):
    context_object_name = "contentinfo_list"
    template_name = "contentinfo_list.html"
    allow_empty = True
    paginate_by = 10

    def get_queryset(self):
        self.name = self.request.GET.get("name", "")
        contentobj = Contentinfo.objects.filter(name__contains=self.name)
        # contentobj = Contentinfo.objects.all()
        return contentobj


class ContentinfoGetChildren(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        try:

            result_dict = {1: 2, 3: 4}
            return result_dict
        except:
            traceback.print_exc()

    def post(self, request, *args, **kwargs):
        try:
            action = self.request.POST.get("action", "")
            action = "org_select"

            self.result_dict = dict()
            self.result_dict["data"] = {"1": {"text": "all contents", "type": "folder", "value": 1,
                                              "additionalParameters": {"children": {
                                                  "2": {"text": "MMMMMMM", "type": "folder", "value": 2,
                                                        "additionalParameters": {"children": {
                                                            "8": {"text": "Source11", "type": "folder", "value": 8,
                                                                  "additionalParameters": {"children": {
                                                                      "9": {"text": "Source1111", "type": "folder",
                                                                            "value": 9,
                                                                            "additionalParameters": {"children": {
                                                                                "17": {"text": "324", "type": "folder",
                                                                                       "value": 17,
                                                                                       "additionalParameters": {
                                                                                           "children": {
                                                                                               "18": {
                                                                                                   "text": "fasdfasdfs",
                                                                                                   "type": "folder",
                                                                                                   "value": 18,
                                                                                                   "additionalParameters": {
                                                                                                       "children": {
                                                                                                           "19": {
                                                                                                               "text": "aaa",
                                                                                                               "type": "folder",
                                                                                                               "value": 19,
                                                                                                               "additionalParameters": {
                                                                                                                   "children": {
                                                                                                                       "20": {
                                                                                                                           "text": "bbb",
                                                                                                                           "type": "folder",
                                                                                                                           "value": 20,
                                                                                                                           "additionalParameters": {
                                                                                                                               "children": {}}}}}}}}}}}},
                                                                                "10": {"text": "Source1232",
                                                                                       "type": "folder",
                                                                                       "value": 10,
                                                                                       "additionalParameters": {
                                                                                           "children": {}}}}}}}}}}}},
                                                  "3": {"text": "BBBBBBB", "type": "folder", "value": 3,
                                                        "additionalParameters": {"children": {
                                                            "16": {"text": "SourceCCCC", "type": "folder", "value": 16,
                                                                   "additionalParameters": {"children": {}}},
                                                            "15": {"text": "SourceBBBB", "type": "folder", "value": 15,
                                                                   "additionalParameters": {"children": {}}}}}},
                                                  "4": {"text": "KKKKK", "type": "folder", "value": 4,
                                                        "additionalParameters": {"children": {
                                                            "6": {"text": "Test1", "type": "folder", "value": 6,
                                                                  "additionalParameters": {"children": {
                                                                      "11": {"text": "Source232323", "type": "folder",
                                                                             "value": 11,
                                                                             "additionalParameters": {
                                                                                 "children": {}}}}}}}}},
                                                  "5": {"text": "AAAA", "type": "folder", "value": 5,
                                                        "additionalParameters": {"children": {
                                                            "14": {"text": "SourceAAAA", "type": "folder", "value": 14,
                                                                   "additionalParameters": {"children": {}}},
                                                            "7": {"text": "test2", "type": "folder", "value": 7,
                                                                  "additionalParameters": {"children": {
                                                                      "12": {"text": "Source2328888", "type": "folder",
                                                                             "value": 12,
                                                                             "additionalParameters": {"children": {
                                                                                 "13": {"text": "Source232324233424",
                                                                                        "type": "folder",
                                                                                        "value": 13,
                                                                                        "additionalParameters": {
                                                                                            "children": {}}}}}}}}}}}}}}}}
            self.result_dict["status"] = "OK"
            result = json.dumps(self.result_dict)
            return HttpResponse(result)
        except:
            traceback.print_exc()


class ContentinfoCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = "contentinfo_edit.html"
    success_url = "/contentinfo/list"
    model = Contentinfo
    fields = "__all__"
    success_message = u"%(name)s 成功创建"

    def form_valid(self, form):
        try:
            name = self.request.POST.get("name", "")
            type = self.request.POST.get("type", "")
            serverid = self.request.POST.get("serverid", "")
            changeflag = self.request.POST.get("serverid", "")
            oldproperty = self.request.POST.get("serverid", "")
            newproperty = self.request.POST.get("serverid", "")
            flag = self.request.POST.get("serverid", "")
            writetime = self.request.POST.get("serverid", "")

            form.instance.name = name
            form.instance.type = type
            form.instance.serverid = serverid
            form.instance.changeflag = changeflag
            form.instance.oldproperty = oldproperty
            form.instance.newproperty = newproperty
            form.instance.flag = flag
            form.instance.writetime = writetime
            return super(ContentinfoCreate, self).form_valid(form)
        except:
            traceback.print_exc()


class ContentinfoChartA(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        try:
            template_name = "contentinfo_chart3.html"
            result_dict = {"datas": [{'path': '/', 'ftype': '1', 'changeflag': '0', 'name': '/'}], "links": []}
            all_content_list = Contentinfo.objects.all()
            b = 0
            namelist = []
            for content in all_content_list:
                if b > 100:
                    break
                datadict = {}
                linkdict = {}
                name = content.name
                path = content.absname
                superid = content.superid
                ftype = content.ftype
                changeflag = content.changeflag
                datadict["label"] = str(name)
                datadict["name"] = str(path)
                datadict["path"] = str(path)
                datadict["ftype"] = str(ftype)
                datadict["changeflag"] = str(changeflag)
                if str(changeflag) == "0":
                    datadict["category"] = 0
                if str(changeflag) == "1":
                    datadict["category"] = 1
                if str(changeflag) == "2":
                    datadict["category"] = 2
                if str(changeflag) == "3":
                    datadict["category"] = 3
                datadict["symbol"] = "circle"
                datadict["symbolSize"] = "30"
                linkdict["source"] = str(path)
                linkdict["target"] = str(superid)
                if str(path) not in namelist:
                    result_dict["datas"].append(datadict)
                    result_dict["links"].append(linkdict)
                namelist.append(str(path))
                b += 1

            return render_to_response(template_name, result_dict)
        except:
            traceback.print_exc()

    def post(self, request, *args, **kwargs):
        try:
            action = self.request.POST.get("action", "")
            action = "org_select"

            """
             {
             "datas":
             [
             {
				name:"aaa",
				path:"root",
				symbol:"circle",
				symbolSize:60,
				value:"sss",

			},
			{
				name:"bbb",
				path:"aaa/bbb",
				symbolSize:42,
				value:"bbb",

			}
			],
			"links":
			[
			{
				source: "bbb",
				target: "aaa",
				lineStyle:{
					normal:{
						color:"#c23531"
					}
				}
			},
			{
				source: "aaa",
				target: "ccc"
			}

			]
			}，最终返回数据结构
			"""

            if action == "org_select":  # 取架构数据
                all_content_list = Contentinfo.objects.all()
                self.result_dict = {"datas": [], "links": []}
                if not all_content_list:
                    default_dict = {"datas": [], "links": []}
                    self.result_list.append(default_dict)
                else:
                    for content in all_content_list:
                        datadict = {}
                        linkdict = {}
                        name = content.name
                        path = content.absname
                        superid = content.superid
                        ftype = content.ftype
                        changeflag = content.changeflag
                        datadict["name"] = name
                        datadict["path"] = path
                        datadict["ftype"] = ftype
                        datadict["changeflag"] = changeflag
                        linkdict["source"] = path
                        linkdict["target"] = superid
                        self.result_dict["datas"].append(datadict)
                        self.result_dict["links"].append(linkdict)
            return HttpResponse(self.result_dict)
        except:
            traceback.print_exc()

# datadepth 是干什么的 没看懂
datadepth = 5
# depthlist 是干什么的 没看懂
depthlist = []
nodenumber = 0
normalnodenumber = 0
addnodenumber = 0
changenodenumber = 0
deletenodenumber = 0

# Bug!!!!!!!!!!画5层，有bug
#1. datadepth=5并不能控制深度小于5
def getDataDict(contentdict={}, serverid=1):
    #获取目录下的所有目录和文件属性
    content = Contentinfo.objects.get(absname=contentdict["absname"], serverid=serverid)
    childcontents = Contentinfo.Children(content)
    nodemaximum = Systeminfo.get_param_value("nodemaximum", "1")
    if nodemaximum:
        nodemaximum = int(nodemaximum)
    else:
        nodemaximum = 10

    if childcontents.count() > nodemaximum:
        childcontents = childcontents[:nodemaximum]
    global datadepth
    global depthlist
    global nodenumber
    global normalnodenumber
    global addnodenumber
    global changenodenumber
    global deletenodenumber

    for childcontent in childcontents:
        if datadepth > 5:
            continue
        changeflag = random.randint(0, 4)
        temp_contentdict = {}
        # 非叶子节点
        if Contentinfo.Children(childcontent):
            temp_contentdict["name"] = str(childcontent.name)
            temp_contentdict["absname"] = str(childcontent.absname)
            temp_contentdict["ftype"] = str(childcontent.ftype)
            temp_contentdict["changeflag"] = str(childcontent.changeflag)
            temp_contentdict["children"] = []
            contentdict["children"].append(temp_contentdict)
            nodenumber += 1
            if childcontent.changeflag == "0":
                normalnodenumber += 1
            elif childcontent.changeflag == "1":
                addnodenumber += 1
            elif childcontent.changeflag == "2":
                changenodenumber += 1
            elif childcontent.changeflag == "3":
                deletenodenumber += 1

            if childcontent.absname not in depthlist:
                depthlist.append(childcontent.absname)
            getDataDict(temp_contentdict, serverid)
            if childcontent.superid not in depthlist:
                datadepth += 1
        # 叶子结点
        else:
            temp_contentdict["name"] = str(childcontent.name)
            temp_contentdict["absname"] = str(childcontent.absname)
            temp_contentdict["ftype"] = str(childcontent.ftype)
            temp_contentdict["changeflag"] = str(childcontent.changeflag)
            temp_contentdict["children"] = []
            contentdict["children"].append(temp_contentdict)
            nodenumber += 1
            if childcontent.changeflag == "0":
                normalnodenumber += 1
            elif childcontent.changeflag == "1":
                addnodenumber += 1
            elif childcontent.changeflag == "2":
                changenodenumber += 1
            elif childcontent.changeflag == "3":
                deletenodenumber += 1
    return contentdict


class ContentinfoChart(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        try:
            template_name = "contentinfo_chart3.html"
            result_dict = {"datas": {"name": "/", "children": []}}
            result_dict = {}
            global datadepth
            datadepth = 0
            global nodenumber
            nodenumber = 0
            global depthlist
            depthlist = []
            rootdict = {}
            datadict = {}
            absname = ""

            login_user = self.request.user
            chartspeed = 1
            from modules.serverinfo.models import ContentSetinfo
            from modules.systeminfo.models import Systeminfo

            systeminfo = Systeminfo.objects.filter(param_name="chartspeed")
            if systeminfo:
                chartspeed = int(systeminfo[0].param_value)
            systeminfo = Systeminfo.objects.filter(param_name="chartinterval")
            if systeminfo:
                chartinterval = int(systeminfo[0].param_value)

            contentset = ContentSetinfo.objects.filter(user=login_user)
            if contentset:
                absname = contentset[0].absname
            try:
                content = Contentinfo.objects.get(absname=absname)
            except:
                content = None
            if content:
                rootdict["name"] = str(content.name)
                rootdict["absname"] = str(content.absname)
                rootdict["ftype"] = str(content.ftype)
                rootdict["changeflag"] = str(content.changeflag)
                rootdict["children"] = []
                datadict = getDataDict(rootdict)
            result_dict["datas"] = datadict
            result_dict["datadepth"] = datadepth
            result_dict["nodenumber"] = nodenumber
            result_dict["chartspeed"] = chartspeed
            result_dict["chartinterval"] = chartspeed
            return render_to_response(template_name, result_dict)
        except:
            traceback.print_exc()

    def post(self, request, *args, **kwargs):
        try:
            action = self.request.POST.get("action", "")
            action = "org_select"

            if action == "org_select":  # 取架构数据
                all_content_list = Contentinfo.objects.all()
                self.result_dict = {"datas": [], "links": []}
                if not all_content_list:
                    default_dict = {"datas": [], "links": []}
                    self.result_list.append(default_dict)
                else:
                    for content in all_content_list:
                        datadict = {}
                        linkdict = {}
                        name = content.name
                        path = content.absname
                        superid = content.superid
                        ftype = content.ftype
                        changeflag = content.changeflag
                        datadict["name"] = name
                        datadict["path"] = path
                        datadict["ftype"] = ftype
                        datadict["changeflag"] = changeflag
                        linkdict["source"] = path
                        linkdict["target"] = superid
                        self.result_dict["datas"].append(datadict)
                        self.result_dict["links"].append(linkdict)
            return HttpResponse(self.result_dict)
        except:
            traceback.print_exc()


class ContentinfoUser(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        try:
            template_name = "contentinfo_user.html"
            result_dict = {"datas": {"name": "/", "children": []}}
            result_dict = {}
            global datadepth
            datadepth = 0
            global nodenumber
            nodenumber = 0
            global normalnodenumber
            normalnodenumber = 0
            global addnodenumber
            addnodenumber = 0
            global changenodenumber
            changenodenumber = 0
            global deletenodenumber
            deletenodenumber = 0
            global depthlist
            depthlist = []
            rootdict = {}
            datadict = {}
            absname = ""

            login_user = self.request.user
            chartspeed = 5
            from modules.serverinfo.models import ContentSetinfo
            from modules.systeminfo.models import Systeminfo

            systeminfo = Systeminfo.objects.filter(param_name="chartspeed")
            if systeminfo:
                chartspeed = int(systeminfo[0].param_value)
            systeminfo = Systeminfo.objects.filter(param_name="chartinterval")
            if systeminfo:
                chartinterval = int(systeminfo[0].param_value)

            contentset = ContentSetinfo.objects.filter(user=login_user)
            if contentset:
                absname = contentset[0].absname

            try:
                content = Contentinfo.objects.get(absname=absname)
            except:
                content = None
            if content:
                rootdict["name"] = str(content.name)
                rootdict["absname"] = str(content.absname)
                rootdict["ftype"] = str(content.ftype)
                rootdict["changeflag"] = str(content.changeflag)
                rootdict["children"] = []
                datadict = getDataDict(rootdict)
            result_dict["datas"] = datadict
            result_dict["datadepth"] = datadepth
            result_dict["nodenumber"] = nodenumber
            result_dict["chartspeed"] = chartspeed
            result_dict["chartinterval"] = chartspeed
            result_dict["normalnodenumber"] = normalnodenumber
            result_dict["addnodenumber"] = addnodenumber
            result_dict["changenodenumber"] = changenodenumber
            result_dict["deletenodenumber"] = deletenodenumber

            return render_to_response(template_name, result_dict)
        except:
            traceback.print_exc()

    def post(self, request, *args, **kwargs):
        try:
            action = self.request.POST.get("action", "")
            action = "org_select"

            if action == "org_select":  # 取架构数据
                all_content_list = Contentinfo.objects.all()
                self.result_dict = {"datas": [], "links": []}
                if not all_content_list:
                    default_dict = {"datas": [], "links": []}
                    self.result_list.append(default_dict)
                else:
                    for content in all_content_list:
                        datadict = {}
                        linkdict = {}
                        name = content.name
                        path = content.absname
                        superid = content.superid
                        ftype = content.ftype
                        changeflag = content.changeflag
                        datadict["name"] = name
                        datadict["path"] = path
                        datadict["ftype"] = ftype
                        datadict["changeflag"] = changeflag
                        linkdict["source"] = path
                        linkdict["target"] = superid
                        self.result_dict["datas"].append(datadict)
                        self.result_dict["links"].append(linkdict)
            return HttpResponse(self.result_dict)
        except:
            traceback.print_exc()

def getDataDict_gh(contentdict={}, serverid=1):
    #获取目录下的所有目录和文件属性

    content = Contentinfo.objects.get(absname=contentdict["absname"], serverid=serverid)
    content_absname = str(content.absname)
    # 根据绝对路径字符串匹配，判断当前目录是否大于5层，如果大于，则不再寻找子节点。
    if len(content_absname.replace(rootname, '', 1).split('/')) >= 5:
        return
    childcontents = Contentinfo.Children(content)
    nodemaximum = Systeminfo.get_param_value("nodemaximum", "1")
    if nodemaximum:
        nodemaximum = int(nodemaximum)
    else:
        nodemaximum = 10

    if childcontents.count() > nodemaximum:
        childcontents = childcontents[:nodemaximum]
    #global depthlist
    global nodenumber
    global normalnodenumber
    global addnodenumber
    global changenodenumber
    global deletenodenumber
    for childcontent in childcontents:

        changeflag = random.randint(0, 4)
        temp_contentdict = {}

        # 非叶子节点
        if Contentinfo.Children(childcontent):

            #print str(childcontent.absname)
            temp_contentdict["name"] = str(childcontent.name)
            temp_contentdict["absname"] = str(childcontent.absname)
            temp_contentdict["ftype"] = str(childcontent.ftype)
            temp_contentdict["changeflag"] = str(childcontent.changeflag)
            temp_contentdict["children"] = []
            contentdict["children"].append(temp_contentdict)
            nodenumber += 1
            if childcontent.changeflag == "0":
                normalnodenumber += 1
            elif childcontent.changeflag == "1":
                addnodenumber += 1
            elif childcontent.changeflag == "2":
                changenodenumber += 1
            elif childcontent.changeflag == "3":
                deletenodenumber += 1
            getDataDict_gh(temp_contentdict, serverid)

        # 叶子结点
        else:
            temp_contentdict["name"] = str(childcontent.name)
            temp_contentdict["absname"] = str(childcontent.absname)
            temp_contentdict["ftype"] = str(childcontent.ftype)
            temp_contentdict["changeflag"] = str(childcontent.changeflag)
            temp_contentdict["children"] = []
            contentdict["children"].append(temp_contentdict)
            nodenumber += 1
            if childcontent.changeflag == "0":
                normalnodenumber += 1
            elif childcontent.changeflag == "1":
                addnodenumber += 1
            elif childcontent.changeflag == "2":
                changenodenumber += 1
            elif childcontent.changeflag == "3":
                deletenodenumber += 1
    return contentdict


#增加rootname = 根目录的absname
rootname = ''

class ContentinfoServer(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        try:
            template_name = "contentinfo_server.html"
            result_dict = {"datas": {"name": "/", "children": []}}
            result_dict = {}

            # initiate rootname in this function
            global rootname

            global datadepth
            datadepth = 0
            global nodenumber
            nodenumber = 0
            global depthlist
            depthlist = []
            rootdict = {}
            datadict = {}
            absname = ""
            serverid = request.GET.get("serverid", 1)
            chartspeed = 5
            from modules.serverinfo.models import ContentSetinfo
            from modules.systeminfo.models import Systeminfo

            systeminfo = Systeminfo.objects.filter(param_name="chartspeed")
            if systeminfo:
                chartspeed = int(systeminfo[0].param_value)
            systeminfo = Systeminfo.objects.filter(param_name="chartinterval")
            if systeminfo:
                chartinterval = int(systeminfo[0].param_value)

            contentset = ContentSetinfo.objects.filter(serverid=serverid)
            if contentset:
                absname = contentset[0].absname
            try:
                content = Contentinfo.objects.get(absname=absname, serverid=serverid)
            except:
                content = None
            if content:

                # initiate rootname
                rootname = str(content.absname)

                rootdict["name"] = str(content.name)
                rootdict["absname"] = str(content.absname)
                rootdict["ftype"] = str(content.ftype)
                rootdict["changeflag"] = str(content.changeflag)
                rootdict["children"] = []
                datadict = getDataDict_gh(rootdict, serverid)
            result_dict["datas"] = datadict
            result_dict["datadepth"] = datadepth
            result_dict["nodenumber"] = nodenumber
            result_dict["chartspeed"] = chartspeed
            result_dict["chartinterval"] = chartspeed
            print nodenumber
            return render_to_response(template_name, result_dict)
        except:
            traceback.print_exc()

    def post(self, request, *args, **kwargs):
        try:
            action = self.request.POST.get("action", "")
            action = "org_select"

            if action == "org_select":  # 取架构数据
                all_content_list = Contentinfo.objects.all()
                self.result_dict = {"datas": [], "links": []}
                if not all_content_list:
                    default_dict = {"datas": [], "links": []}
                    self.result_list.append(default_dict)
                else:
                    for content in all_content_list:
                        datadict = {}
                        linkdict = {}
                        name = content.name
                        path = content.absname
                        superid = content.superid
                        ftype = content.ftype
                        changeflag = content.changeflag
                        datadict["name"] = name
                        datadict["path"] = path
                        datadict["ftype"] = ftype
                        datadict["changeflag"] = changeflag
                        linkdict["source"] = path
                        linkdict["target"] = superid
                        self.result_dict["datas"].append(datadict)
                        self.result_dict["links"].append(linkdict)
            return HttpResponse(self.result_dict)
        except:
            traceback.print_exc()


class ContentinfoUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = "contentinfo_edit.html"
    success_url = "/contentinfo/list"
    model = Contentinfo
    fields = ["name", "superid", "serverid", "changeflag", "checkflag"]
    success_message = u" 修改成功"

    def get_context_data(self, **kwargs):
        context = super(ContentinfoUpdate, self).get_context_data(**kwargs)
        context["form_content"] = u"编辑资源信息"
        return context
