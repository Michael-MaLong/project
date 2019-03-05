# coding=utf-8
from django.test import TestCase

# Create your tests here.

import paramiko
import os
from  stat import *
#
# remote_path = r'/home/redhat/tomcat-8.5.14'
#
# contentid = 1
# rootdict = {
#     "id": 1,
#     "name": "tomcat-8.5.14",
#     "absname": '/home/redhat/tomcat-8.5.14',
#     "ftype": 1,
#     "changeflag": 0,
#     "childrens": []
# }
#
# host_ip = '192.168.174.128'
# username = 'redhat'
# password = 'redhat'
# remote_path = r'/home/redhat/tomcat-8.5.14'
#
# t = paramiko.Transport((host_ip, 22))
# t.connect(username=username, password=password)  # 登录远程服务器
# sftp = paramiko.SFTPClient.from_transport(t)   # sftp传输协议


def testA(contentdict={}):
    #获取目录下的所有目录和文件属性
    contents = sftp.listdir_attr(contentdict["absname"])

    #循环处理所有目录和文件放到当前字典的childrens列表中
    for content in contents:
        temp_contentdict = {}
        if S_ISDIR(content.st_mode):
            temp_contentdict["name"] = content.filename
            temp_contentdict["absname"] = contentdict["absname"] + "/" + content.filename
            temp_contentdict["ftype"] = 1
            temp_contentdict["childrens"] = []
            contentdict["childrens"].append(temp_contentdict)
            testA(temp_contentdict)
        else:
            temp_contentdict["name"] = content.filename
            temp_contentdict["absname"] = contentdict["absname"] + '/' + content.filename
            temp_contentdict["ftype"] = 2
            temp_contentdict["childrens"] = []
            contentdict["childrens"].append(temp_contentdict)

    return contentdict


#Adict = testA(rootdict)

remotepath = "/home/redhat/tomcat-8.5.14"




def initRemotePath(remotepath):
    alldir = []
    dirlist = remotepath.split("/")
    templist = dirlist[1:]
    print "ttttttttt", templist
    count = remotepath.count("/")
    pwddir = ""
    for l in range(count):
        i = 1
        tempdir = ""
        for i in range(i):
            tempdir = "/" + templist[l]
            pwddir += tempdir
            i += 1
        alldir.append(pwddir)

    # content = Contentinfo(name=pwddir, type=1, superid=0, serverid=0, changeflag=0, oldproperty=0, newproperty=0,
    #                       flag=0, writetime='00')
    # content.save()



    return alldir


test = initRemotePath(remotepath)
print "========", test

initlist=[]
for t in test:
    dirdict={}
    i=t.rfind("/")
    if i==0:
        dirdict["name"]=t[i:]
        dirdict["absname"]=t
        dirdict["superid"]="/"
    else:
        dirdict["name"]=t[i:]
        dirdict["absname"]=t
        dirdict["superid"]=t[:i]
    initlist.append(dirdict)

print 'IIIIIIIIIIIIIIIII',initlist










