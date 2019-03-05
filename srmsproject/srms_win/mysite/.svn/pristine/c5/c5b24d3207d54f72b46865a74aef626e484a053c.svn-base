# coding=utf-8
from django.test import TestCase

# Create your tests here.

import paramiko
import os

def remote_scp(host_ip,remote_path,local_path,username,password):
    print 'START==========='
    t = paramiko.Transport((host_ip,22))
    t.connect(username=username, password=password)  # 登录远程服务器
    sftp = paramiko.SFTPClient.from_transport(t)   # sftp传输协议
    src = remote_path
    des = local_path
    sftp.get(src,des)
    t.close()
    print 'END==========='


if __name__=='__main__':
    print '================'
    host_ip='192.168.174.128'
    username='redhat'
    password='redhat'
    remote_path='/home/redhat/ccdd.txt'
    local_path=r'D:\MyWorkspace\srms\mysite\media\temp\user_contentinfo\ok.txt'
    remote_scp(host_ip,remote_path,local_path,username,password)