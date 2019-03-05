# coding=utf-8
from django.db import models
from django.core.cache import cache
import traceback

SYSVERSION = 1


class Systeminfo(models.Model):
    PARAMTYPECHOICE = (
        ('1', u'常规'),
        ('2', u'Email'),
        ('3', u'定时任务'),
    )

    param_name = models.CharField(u"参数名", max_length=100)
    param_value = models.CharField(u"参数值", max_length=100)
    param_display = models.CharField(u"参数描述", max_length=100)
    param_type = models.CharField(u"参数类型", max_length=2, choices=PARAMTYPECHOICE)

    def __str__(self):
        return self.param_name + self.param_value

    class Meta:
        verbose_name = u"系统设置"
        index_together = ["id", "param_name"]  # 索引字段组合
        permissions = (
            ("browse_systeminfo", u"授权浏览 系统设置"),
        )

    # 更新系统参数缓存
    def update_systeminfo_cache(self):
        global SYSVERSION
        SYSVERSION += 1

    @staticmethod
    def get_param(param_name):
        global SYSVERSION
        try:
            result = {param_name: ""}
            systeminfo = cache.get("sys_config_%s_%s" % (param_name, SYSVERSION))
            if systeminfo:
                return systeminfo
            systeminfo = Systeminfo.objects.filter(param_name=param_name)
            if systeminfo.exists():
                systeminfo_s = systeminfo[0]
                result = {systeminfo_s.param_name: systeminfo_s.param_value}
                cache.set("all_dept_%s_%s" % (param_name, SYSVERSION), result)
            return result
        except:
            traceback.print_exc()
            return {param_name: ""}

    def save(self, *args, **kwargs):
        global DEPTVERSION
        try:
            self.update_systeminfo_cache()
            super(Systeminfo, self).save(*args, **kwargs)
        except:
            traceback.print_exc()
