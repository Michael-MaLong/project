# coding=utf-8
from django.test import TestCase

# Create your tests here.

import paramiko
import os
from  stat import *


remote_path = r'/home/redhat/tomcat-8.5.14'

contentid = 1
rootdict = {
"id": 1,
"name": "tomcat-8.5.14",
"absname": '/home/redhat/tomcat-8.5.14',
"ftype": 1,
"changeflag": 0,
"childrens": []
}


host_ip = '192.168.174.128'
username = 'redhat'
password = 'redhat'
remote_path = r'/home/redhat/tomcat-8.5.14'

t = paramiko.Transport((host_ip, 22))
t.connect(username=username, password=password)  # 登录远程服务器
sftp = paramiko.SFTPClient.from_transport(t)   # sftp传输协议

def testA(contentdict={}):

    #获取目录下的所有目录和文件属性
    contents = sftp.listdir_attr(contentdict["absname"])

    #循环处理所有目录和文件放到当前字典的childrens列表中
    for content in contents:
        temp_contentdict={}
        if S_ISDIR(content.st_mode):
            temp_contentdict["name"]=content.filename
            temp_contentdict["absname"]=contentdict["absname"]+"/"+content.filename
            temp_contentdict["ftype"]=1
            temp_contentdict["childrens"]=[]
            contentdict["childrens"].append(temp_contentdict)
            testA(temp_contentdict)
        else:
            temp_contentdict["name"]=content.filename
            temp_contentdict["absname"]=contentdict["absname"]+'/'+content.filename
            temp_contentdict["ftype"]=2
            temp_contentdict["childrens"]=[]
            contentdict["childrens"].append(temp_contentdict)

    return contentdict

Adict=testA(rootdict)


print '=========',Adict


