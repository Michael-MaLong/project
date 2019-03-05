# coding=utf-8
from django.test import TestCase

# Create your tests here.



remotepath = "/home/redhat/tomcat-8.5.14"


def initRemotePath(remotepath):
    alldir = []
    count = remotepath.count("/")
    for l in range(count):
        dirdict={}
        i=remotepath.rfind("/")
        if i==0:
            dirdict["superid"]="/"
        else:
            dirdict["superid"]=remotepath[:i]
        dirdict["name"]=remotepath[i+1:]
        dirdict["absname"]=remotepath
        remotepath=remotepath[:i]
        print "RRRRRRRRRRRr",remotepath
        alldir.append(dirdict)
    return alldir


test = initRemotePath(remotepath)
print "========", test
test.reverse()
print "XXXXXXXXXXXXXX", test


