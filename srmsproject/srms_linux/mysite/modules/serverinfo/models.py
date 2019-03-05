# coding=utf-8

from __future__ import unicode_literals
from stat import *
import datetime
import traceback
from django.db import models
import paramiko

remotepathlist = []
sftp = None


class Serverinfo(models.Model):
    """服务器信息"""
    name = models.CharField(u"服务器名称", max_length=100)
    ip = models.CharField(u"IP", max_length=100)
    port = models.CharField(u"端口", max_length=100)
    username = models.CharField(u"用户名称", max_length=100)
    password = models.CharField(u"用户密码", max_length=100)
    writetime = models.CharField(u"更新时间", max_length=100)

    # 连接远程主机
    def connect(self):
        global sftp
        if sftp:
            return sftp
        try:
            host = paramiko.Transport((self.ip, int(self.port)))
            host.connect(username=self.username, password=self.password)  # 登录远程服务器
            sftp = paramiko.SFTPClient.from_transport(host)   # sftp传输协议
        except:
            traceback.print_exc()
        return sftp

    # 获取服务器目录的所有目录和文件属性
    def getDirContent(self, dir):
        print dir
        sftp = self.connect()
        listdir = []
        if sftp:
            listdir = sftp.listdir_attr(dir)
        print listdir
        return listdir


    # 初始化服务器根目录的所有目录和文件属性
    def initContent(self):
        from modules.contentinfo.models import Contentinfo

        filelist = self.getDirContent(r"/")
        for f in filelist:
            if S_ISDIR(f.st_mode):
                ftype = 1
            else:
                ftype = 2
            try:
                content = Contentinfo.objects.get(absname="/" + f.filename, serverid=self.ip)
            except:
                content = None
            if content:
                content.writetime = datetime.datetime.now()
                content.save()
            else:
                content = Contentinfo(name=f.filename, absname="/" + f.filename, ftype=ftype, superid="/",
                                      serverid=self,
                                      changeflag=0,
                                      oldproperty="",
                                      newproperty="", checkflag=0, writetime=datetime.datetime.now())
                content.save()
        return []

    # 初始化服务器指定目录的所有目录
    def initPathContent(self, remotepath):
        from modules.contentinfo.models import Contentinfo

        filelist = []
        count = remotepath.count("/")
        for l in range(count):
            dirdict = {}
            i = remotepath.rfind("/")
            if i == 0:
                dirdict["superid"] = "/"
            else:
                dirdict["superid"] = remotepath[:i]
            dirdict["name"] = remotepath[i + 1:]
            dirdict["absname"] = remotepath
            remotepath = remotepath[:i]
            filelist.append(dirdict)

        for file in filelist:
            try:
                content = Contentinfo.objects.get(absname=file["absname"])
            except:
                content = None
            if not content:
                content = Contentinfo(name=file["name"], absname=file["absname"], ftype=1,
                                      superid=file["superid"],
                                      serverid=self, changeflag=1,
                                      oldproperty="",
                                      newproperty="", checkflag=0, writetime=datetime.datetime.now())
                content.save()

        return "initPathContent==============="

    # 将指定目录下的所有目录和文件格式化为list
    def formatRemotepath(self, remotepath):
        #获取目录下的所有目录和文件属性
        contents = self.connect().listdir_attr(remotepath)

        #循环处理所有目录和文件放到dirlist列表中
        for content in contents:
            print "CCCCCCCCCCCCC"
            temp_contentdict = {}
            if S_ISDIR(content.st_mode):
                temp_contentdict["name"] = content.filename
                temp_contentdict["absname"] = remotepath + "/" + content.filename
                temp_contentdict["ftype"] = 1
                temp_contentdict["st_mtime"] = content.st_mtime
                temp_contentdict["parent"] = remotepath
                remotepathlist.append(temp_contentdict)
                self.formatRemotepath(temp_contentdict["absname"])
            else:
                temp_contentdict["name"] = content.filename
                temp_contentdict["absname"] = remotepath + '/' + content.filename
                temp_contentdict["ftype"] = 2
                temp_contentdict["st_mtime"] = content.st_mtime
                temp_contentdict["parent"] = remotepath
                remotepathlist.append(temp_contentdict)

        return remotepathlist


    # 同步服务器指定监控目录的所有目录和文件
    def syncContent(self, remotepath):
        from modules.contentinfo.models import Contentinfo

        print "11111111111111111"

        filelist = self.formatRemotepath(remotepath)
        for file in filelist:
            print "FFFFFFFFFFFF", file["absname"]
            try:
                content = Contentinfo.objects.get(absname=file["absname"])
            except:
                content = None
            if content:
                if content.oldproperty == file["st_mtime"]:
                    content.changeflag = 0
                else:
                    content.changeflag = 2
            else:
                content = Contentinfo(name=file["name"], absname=file["absname"], ftype=file["ftype"],
                                      superid=file["parent"],
                                      serverid=self, changeflag=1,
                                      oldproperty=0,
                                      newproperty=file["st_mtime"], checkflag=1, writetime=datetime.datetime.now())
            content.save()

        return "syncContent==============="

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"服务器信息"
        index_together = ["name"]  # 索引字段组合
        unique_together = (("ip", ),)
