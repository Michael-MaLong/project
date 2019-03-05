# coding=utf-8
from django.test import TestCase

# Create your tests here.

import paramiko
import os
from  stat import *

# 定义一个类，表示一台远端linux主机
class LinuxServer(object):
    # 通过IP, 用户名，密码，超时时间初始化一个远程Linux主机
    def __init__(self, ip, username, password, timeout=30):
        self.ip = ip
        self.username = username
        self.password = password
        self.timeout = timeout
        # transport和chanel
        self.t = ''
        self.chan = ''
        # 链接失败的重试次数
        self.try_times = 3

    # 调用该方法连接远程主机
    def connect(self):
        pass

    # 断开连接
    def close(self):
        pass

    # 发送要执行的命令
    def send(self, cmd):
        pass

    # get单个文件
    def sftp_get(self, remotefile, localfile):
        t = paramiko.Transport(sock=(self.ip, 22))
        t.connect(username=self.username, password=self.password)
        sftp = paramiko.SFTPClient.from_transport(t)
        sftp.get(remotefile, localfile)
        t.close()

    # put单个文件
    def sftp_put(self, localfile, remotefile):
        t = paramiko.Transport(sock=(self.ip, 22))
        t.connect(username=self.username, password=self.password)
        sftp = paramiko.SFTPClient.from_transport(t)
        sftp.put(localfile, remotefile)
        t.close()


    # ------获取远端linux主机上指定目录及其子目录下的所有文件------
    def __get_all_files_in_remote_dir(self, sftp, remote_dir):
        # 保存所有文件的列表
        all_files = list()

        # 去掉路径字符串最后的字符'/'，如果有的话
        if remote_dir[-1] == '/':
            remote_dir = remote_dir[0:-1]

        # 获取当前指定目录下的所有目录及文件，包含属性值
        files = sftp.listdir_attr(remote_dir)
        for x in files:
            # remote_dir目录中每一个文件或目录的完整路径
            filename = remote_dir + '/' + x.filename
            # 如果是目录，则递归处理该目录，这里用到了stat库中的S_ISDIR方法，与linux中的宏的名字完全一致
            if S_ISDIR(x.st_mode):
                all_files.extend(self.__get_all_files_in_remote_dir(sftp, filename))
            else:
                all_files.append(filename)
        return all_files


    def sftp_get_dir(self, remote_dir, local_dir):
        t = paramiko.Transport(sock=(self.ip, 22))
        t.connect(username=self.username, password=self.password)
        sftp = paramiko.SFTPClient.from_transport(t)

        # 获取远端linux主机上指定目录及其子目录下的所有文件
        all_files = self.__get_all_files_in_remote_dir(sftp, remote_dir)
        # 依次get每一个文件
        for x in all_files:
            filename = x.split('/')[-1]
            local_filename = os.path.join(local_dir, filename)
            print u'Get文件%s传输中...' % filename
            sftp.get(x, local_filename)



            # ------获取本地指定目录及其子目录下的所有文件------

    def __get_all_files_in_local_dir(self, local_dir):
        # 保存所有文件的列表
        all_files = list()

        # 获取当前指定目录下的所有目录及文件，包含属性值
        files = os.listdir(local_dir)
        for x in files:
            # local_dir目录中每一个文件或目录的完整路径
            filename = os.path.join(local_dir, x)
            # 如果是目录，则递归处理该目录
            if os.path.isdir(x):
                all_files.extend(self.__get_all_files_in_local_dir(filename))
            else:
                all_files.append(filename)
        return all_files

    def sftp_put_dir(self, local_dir, remote_dir):
        t = paramiko.Transport(sock=(self.ip, 22))
        t.connect(username=self.username, password=self.password)
        sftp = paramiko.SFTPClient.from_transport(t)

        # 去掉路径字符穿最后的字符'/'，如果有的话
        if remote_dir[-1] == '/':
            remote_dir = remote_dir[0:-1]

        # 获取本地指定目录及其子目录下的所有文件
        all_files = self.__get_all_files_in_local_dir(local_dir)
        # 依次put每一个文件
        for x in all_files:
            filename = os.path.split(x)[-1]
            remote_filename = remote_dir + '/' + filename
            print u'Put文件%s传输中...' % filename
            sftp.put(x, remote_filename)


if __name__ == '__main__':
    remote_path = r'/home/redhat/tomcat-8.5.14'
    local_path = r'D:\MyWorkspace\srms\mysite\media\temp\user_contentinfo'

    host = LinuxServer('192.168.174.128', 'redhat', 'redhat')

    # 将远端remote_path目录中的所有文件get到本地local_path目录
    host.sftp_get_dir(remote_path, local_path)
    # # 将本地local_path目录中的所有文件put到远端remote_path目录
    # host.sftp_put_dir(remote_path, local_path)

'''
# 运行结果
Get文件.profile传输中...
Get文件.inputrc传输中...
Get文件.emacs传输中...
Get文件.bash_history传输中...
Get文件.bashrc传输中...
'''

'''
if __name__ == '__main__':
    remotefile = r'/home/sea/test/xxoo.txt'
    localfile = r'E:\PythonFiles\Learn\ooxx.txt'

    host = LinuxServer('192.168.174.128', 'redhat', 'redhat')

    # 将远端的xxoo.txt get到本地，并保存为ooxx.txt
    host.sftp_get(remotefile, localfile)

    # # 将本地的xxoo.txt put到远端，并保持为xxoo.txt
    # host.sftp_put(localfile, remotefile)

'''