# coding=utf-8

import traceback
# from __future__ import unicode_literals
from django.apps import AppConfig
from django.db.models.signals import post_migrate

def init_system_info(sender, **kwargs):
    """初始化字系统参数
    :param sender:
    :param kwargs:
    :return:
    """
    try:
        init_param_list = [
            {"param_name": "site_name", "param_value": u"服务器资源监控系统", "param_display": u"系统名称", "param_type": "1"},
            {"param_name": "company_name", "param_value": u"国家电网", "param_display": u"公司名称", "param_type": "1"},
            {"param_name": "scheduled_backup", "param_value": "0", "param_display": u"备份数据库间隔(天)", "param_type": "3"},
            {"param_name": "scheduled_clean", "param_value": "0", "param_display": u"清理数据库备份间隔(天)", "param_type": "3"},
        ]
        from modules.systeminfo.models import Systeminfo
        for kwargs in init_param_list:
            systeminfo = Systeminfo.objects.filter(param_name=kwargs["param_name"])
            if not systeminfo.exists():
                Systeminfo.objects.get_or_create(**kwargs)
        print "init system config success......"
    except:
        traceback.print_exc()


class SysteminfoConfig(AppConfig):
    name = 'modules.systeminfo'

    def ready(self):
        post_migrate.connect(init_system_info, sender=self)

