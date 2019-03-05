# coding=utf-8

import json
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.views.generic import View
from django.views.generic import ListView
import datetime
import traceback
from modules.contentinfo.models import Contentinfo
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from modules.serverinfo.models import Serverinfo


class ContentinfoInit(View):
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
            print reverse('contentinfo:contentinfo_list')
            return redirect(reverse('contentinfo:contentinfo_list'))
        except:
            traceback.print_exc()


class ContentinfoPathInit(View):
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


class ContentinfoList(ListView):
    context_object_name = "contentinfo_list"
    template_name = "contentinfo_list.html"
    allow_empty = True
    paginate_by = 10

    def get_queryset(self):
        self.name = self.request.GET.get("name", "")
        contentobj = Contentinfo.objects.filter(name__contains=self.name)
        # contentobj = Contentinfo.objects.all()
        return contentobj


class ContentinfoCreate(SuccessMessageMixin, CreateView):
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


class ContentinfoChartA(View):
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


datadepth = 0


def getDataDict(contentdict={}):
    #获取目录下的所有目录和文件属性
    content = Contentinfo.objects.get(absname=contentdict["absname"])
    childcontents = Contentinfo.Children(content)
    global datadepth
    for childcontent in childcontents:
        temp_contentdict = {}
        if Contentinfo.Children(childcontent):
            temp_contentdict["name"] = str(childcontent.name)
            temp_contentdict["absname"] = str(childcontent.absname)
            temp_contentdict["ftype"] = str(childcontent.ftype)
            temp_contentdict["changeflag"] = str(childcontent.changeflag)
            temp_contentdict["children"] = []
            contentdict["children"].append(temp_contentdict)
            getDataDict(temp_contentdict)
            datadepth += 1
        else:
            temp_contentdict["name"] = str(childcontent.name)
            temp_contentdict["absname"] = str(childcontent.absname)
            temp_contentdict["ftype"] = str(childcontent.ftype)
            temp_contentdict["changeflag"] = str(childcontent.changeflag)
            temp_contentdict["children"] = []
            contentdict["children"].append(temp_contentdict)

    return contentdict


class ContentinfoChart(View):
    def get(self, request, *args, **kwargs):
        try:
            template_name = "contentinfo_chart3.html"
            result_dict = {"datas": {"name": "/", "children": []}}
            result_dict = {}
            print result_dict
            absname = "/home/redhat/tomcat-8.5.14/webapps/ace/assets"
            rootdict = {}
            absname = "/home/redhat/.gconf"
            print absname
            content = Contentinfo.objects.filter(absname=absname)[0]
            print content

            rootdict["name"] = str(content.name)
            rootdict["absname"] = str(content.absname)
            rootdict["ftype"] = str(content.ftype)
            rootdict["changeflag"] = str(content.changeflag)
            rootdict["children"] = []
            global datadepth
            datadepth = 0
            datadict = getDataDict(rootdict)
            result_dict["datas"] = datadict
            result_dict["datadepth"] = datadepth
            return render_to_response(template_name,result_dict)
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


class ContentinfoUser(View):
    def get(self, request, *args, **kwargs):
        try:
            template_name = "contentinfo_user.html"
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

