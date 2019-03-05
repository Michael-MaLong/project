# coding=utf-8
from django.test import TestCase

# Create your tests here.

import paramiko
import os
from  stat import *


host_ip = '192.168.174.128'
username = 'redhat'
password = 'redhat'

t = paramiko.Transport((host_ip, 22))
t.connect(username=username, password=password)  # 登录远程服务器
sftp = paramiko.SFTPClient.from_transport(t)   # sftp传输协议


rootdict = {
"id": 1,
"name": "/",
"absname": '/home/redhat/tomcat-8.5.14',
"ftype": 1,
"changeflag": 0,
"parent": "/"
}


dictlist=[]
def testB(rootdict):

    #获取目录下的所有目录和文件属性
    contents = sftp.listdir_attr(rootdict["absname"])

    #循环处理所有目录和文件放到dirlist列表中
    for content in contents:
        temp_contentdict={}
        if S_ISDIR(content.st_mode):
            temp_contentdict["name"]=content.filename
            temp_contentdict["absname"]=rootdict["absname"]+"/"+content.filename
            temp_contentdict["ftype"]=1
            temp_contentdict["parent"]=rootdict["absname"]
            dictlist.append(temp_contentdict)
            try:
                testB(temp_contentdict)
            except Exception,ee:
                print 'EEEEEEEEEEEEEE',ee
                pass
        else:
            temp_contentdict["name"]=content.filename
            temp_contentdict["absname"]=rootdict["absname"]+'/'+content.filename
            temp_contentdict["ftype"]=2
            temp_contentdict["parent"]=rootdict["absname"]
            dictlist.append(temp_contentdict)
    return dictlist

blist=testB(rootdict)
aa=0
for b in blist:
    aa+=1
    print 'XXXXXXXXXXXX',aa
    print '============',b


