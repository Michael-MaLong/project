# coding=utf-8

from fabric.api import *
from fabric.colors import *

env.hosts = ['192.168.174.128']
env.user = 'redhat'
env.password = 'redhat'


def task():
    print 'AAAAAAA'
    get(r'/home/redhat/tomcat-8.5.14/webapps/ace', r'D:\MyWorkspace\srms\mysite\media\temp\user_contentinfo')

task()
