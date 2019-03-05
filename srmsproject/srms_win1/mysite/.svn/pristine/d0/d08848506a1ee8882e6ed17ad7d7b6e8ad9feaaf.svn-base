# coding=utf-8
from django import template

register = template.Library()

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