# coding=utf-8
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
import traceback
from django.db.models import Q


class ProfileBase(type):  # 对于传统类，他们的元类都是types.ClassType
    def __new__(cls, name, bases, attrs):  # 带参数的构造器，__new__一般用于设置不变数据类型的子类
        module = attrs.pop('__module__')
        parents = [b for b in bases if isinstance(b, ProfileBase)]
        if parents:
            fields = []
            for obj_name, obj in attrs.items():
                if isinstance(obj, models.Field): fields.append(obj_name)
                User.add_to_class(obj_name, obj)
            UserAdmin.fieldsets = list(UserAdmin.fieldsets)
            UserAdmin.fieldsets.append((name, {'fields': fields}))
        return super(ProfileBase, cls).__new__(cls, name, bases, attrs)


class ProfileUser(object):
    __metaclass__ = ProfileBase  # 类属性


GENDER_CHOICES = (
    ('M', u'男'),
    ('F', u'女'),
)


class Userinfo(ProfileUser):
    """管理员扩展信息"""
    gender = models.CharField(u"性别", max_length=2, choices=GENDER_CHOICES, blank=True)
    mobile_phone = models.CharField(u"电话", max_length=11, blank=True)
    photo = models.ImageField(u"头像", upload_to='user_photo', default='/static/avatars/avatar2.png', blank=True)
    remark1 = models.CharField(u"备注1", max_length=256, blank=True)
    remark2 = models.CharField(u"备注2", max_length=256, blank=True)
    writetime = models.CharField(u"更新时间", max_length=100)
    USERNAME_FIELD = 'username'
    FIRST_NAME_FIELD = 'first_name'


    class Meta:
        verbose_name = u"用户信息"
        ordering = ['-id']  # id倒叙

