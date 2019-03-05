# coding=utf-8
from django import template
import traceback
import datetime
from django.utils import timezone
from modules.systeminfo.models import Systeminfo

register = template.Library()

"""
1：字符串"true"转bool型True
2：字符串时间"2016-01-14"转datetime型时间
3：bool型True转字符串，是/否
"""


@register.filter
def bool_formater(bool_str=""):
    """格式化字符串
    :param bool_str:字符串
    :return:True/False
    """
    try:
        if bool_str == "true":
            return True
        if bool_str == "false":
            return False
        if not bool_str:
            return False
    except:
        traceback.print_exc()


@register.filter
def date_formater(date_str, formatstr):
    """格式化时间
    :param date_str: "2016-01-14"
    :param formatstr: "%Y-%m-%d"
    :return:datetime型时间
    """
    try:
        if date_str:
            return datetime.datetime.strptime(date_str, formatstr).replace(tzinfo=timezone.utc)
        else:
            return timezone.now()
    except:
        traceback.print_exc()


@register.filter
def true_false_formater(value):
    """格式化为是/否
    :param value:bool型，
    :return: 是/否
    """

    try:
        if value:
            return r'<i class="green ace-icon fa fa-check-circle bigger-130"></i>'
        return r'<i class="red ace-icon fa fa-times-circle bigger-130"></i>'
    except:
        traceback.print_exc()


@register.filter
def true_false_unformat(str_param):
    try:
        if str_param == u"是":
            return True
        if str_param == u"否":
            return False

    except:
        traceback.print_exc()
        return False


@register.assignment_tag
def get_system_param(param_name):
    try:
        return Systeminfo.get_param(param_name).get(param_name, "")
    except:
        traceback.print_exc()
        return ""


BoolDict = {
    "0": u"否",
    "1": u"是",
}


@register.filter
def isYesNo(value):
    if value:
        return BoolDict['1']
    return BoolDict['0']


@register.filter('truncate_chars')
def truncate_chars(value):
    """
    若字符串长度大于30，则省略之后的内容，否则原样输出该字符串。
    :param value:
    :return:
    """
    if value.__len__() > 30:
        return '%s......' % value[0:30]
    else:
        return value