# coding=utf-8

from __future__ import unicode_literals

from django.db import models

from django.utils import timezone
# Create your models here.
from modules.serverinfo.models import Serverinfo

CHANGE_CHOICES = (
    ('0', u'正常'),
    ('1', u'新增'),
    ('2', u'变更'),
    ('3', u'删除'),
    ('4', u'变更+'),
)

CHECK_CHOICES = (
    ('0', u'否'),
    ('1', u'是'),
)

class Contentinfo(models.Model):
    """服务器资源信息"""
    name = models.CharField(u"资源名称", max_length=100)
    absname = models.CharField(u"资源路径", max_length=300)
    ftype = models.CharField(u"资源类型", max_length=100)
    superid = models.CharField(u"上级资源id", max_length=300)
    serverid = models.ForeignKey(Serverinfo, null=True, blank=True)
    changeflag = models.CharField(u"变更状态", max_length=2, choices=CHANGE_CHOICES, blank=True) #0 代表无变更；1 代表新增；2 代表变更；3 代表删除；4 代表子节点有变更
    oldproperty = models.CharField(u"原资源属性", max_length=100)
    newproperty = models.CharField(u"新资源属性", max_length=100)
    checkflag = models.CharField(u"是否监控", max_length=2, choices=CHECK_CHOICES, blank=True)#0 代表不监控；1 代表监控；
    writetime = models.DateTimeField(u"更新时间", default=timezone.now, null=False, blank=False)

    def Children(self):
        return Contentinfo.objects.filter(superid=self.absname)

    def AllChildren(self, start=[]):
        for d in self.Children():
            if d not in start:
                start.append(d)
                d.AllChildren(start)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"资源信息"
        index_together = ["name"]  # 索引字段组合
        unique_together = (("absname", "serverid" ),)


