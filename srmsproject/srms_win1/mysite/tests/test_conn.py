# coding=utf-8

import paramiko

host_ip = '192.168.174.128'
username = 'redhat'
password = 'redhat'

t = paramiko.Transport((host_ip, 22))
t.connect(username=username, password=password)  # 登录远程服务器
sftp = paramiko.SFTPClient.from_transport(t)   # sftp传输协议

print '=========',sftp


