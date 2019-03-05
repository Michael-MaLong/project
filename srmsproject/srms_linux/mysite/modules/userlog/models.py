# coding=utf-8

from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Userlog(models.Model):
    """用户日志信息"""
    User = models.ForeignKey(User, verbose_name=u"用户", null=True, blank=True)
    opmodel = models.CharField(u"类型", max_length=40, null=True, blank=True)
    opaction = models.CharField(u"动作", max_length=40, default="Modify", null=False, blank=False)
    opobject = models.CharField(u"对象", max_length=100, null=True, blank=True)
    writetime = models.DateTimeField(u"更新时间", default=timezone.now, null=False, blank=False)

    def __str__(self):
        return self.User.username+self.opobject

    class Meta:
        verbose_name = u"日志信息"
        index_together = ["id"]  # 索引字段组合
        unique_together = (("id", ),)

