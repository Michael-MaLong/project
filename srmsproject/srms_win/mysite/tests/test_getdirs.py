# coding=utf-8
from django.test import TestCase

# Create your tests here.

import paramiko
import os
from  stat import *


def remote_scp(host_ip, remote_path, local_path, username, password):
    print 'START==========='
    t = paramiko.Transport((host_ip, 22))
    t.connect(username=username, password=password)  # 登录远程服务器
    sftp = paramiko.SFTPClient.from_transport(t)   # sftp传输协议
    src = remote_path
    des = local_path
    all_files = list()
    filelist = sftp.listdir_attr(remote_path)
    for x in filelist:
        filename = remote_path + '/' + x.filename
        if S_ISDIR(x.st_mode):
            all_files.extend()
        else:
            all_files.append(filename)
        print x.st_size,x.st_uid,x.st_gid,x.st_mode,x.st_atime,x.st_mtime,x.filename,'xxxxxxxxxxxx',x.attr,'===========',filename


    #sftp.get(src, des)
    t.close()
    print 'END==========='


if __name__ == '__main__':
    print '================'
    host_ip = '192.168.174.128'
    username = 'redhat'
    password = 'redhat'
    remote_path = r'/home/redhat/tomcat-8.5.14'
    local_path = r'D:\MyWorkspace\srms\mysite\media\temp\user_contentinfo\ok.txt'
    remote_scp(host_ip, remote_path, local_path, username, password)