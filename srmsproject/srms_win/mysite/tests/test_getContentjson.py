# coding=utf-8
from django.test import TestCase
from modules.contentinfo.models import Contentinfo


def testA(contentdict={}):
    #获取目录下的所有目录和文件属性
    content = Contentinfo.objects.get(contentdict["absname"])
    childcontents = Contentinfo.Children(content)

    for childcontent in childcontents:
        temp_contentdict = {}
        if Contentinfo.Children(childcontents):
            temp_contentdict["name"] = childcontent.name
            temp_contentdict["absname"] = childcontent.absname
            temp_contentdict["childrens"] = []
            contentdict["childrens"].append(temp_contentdict)
            testA(temp_contentdict)
        else:
            temp_contentdict["name"] = childcontent.name
            temp_contentdict["absname"] = childcontent.absname
            temp_contentdict["childrens"] = []
            contentdict["childrens"].append(temp_contentdict)

    return contentdict


rootdict = {"name": "redhat", "absname": "/home/redhat", "children": []}
Adict = testA(rootdict)











