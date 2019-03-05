# coding=utf-8
import traceback
from modules.contentinfo.models import Contentinfo
from modules.serverinfo.models import Serverinfo

# 获取动态查询条件
def get_kwargs(param):
    """组装查询条件集合
    :param param:
    :return:
    """
    kwargs = dict()
    try:
        [kwargs.update({query_field: param}) for query_field, param in param.items() if param]
    except:
        traceback.print_exc()
    return kwargs


#
def initServerContent():
    pass

    return


# 初始化服务器资源信息
def initServerContent():
    pass

    return
