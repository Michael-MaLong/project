# coding=utf-8

import datetime
import random
from modules.contentinfo.models import Contentinfo
from modules.serverinfo.models import Serverinfo

originStr = "abcdefghijklmnopqrstuvwxyz"
serverobj = Serverinfo.objects.all()[0]

for i in range(10000000):
    r = random.randint(1, 23)
    namestr = originStr[0:r]+"=="+str(i)
    # print namestr, 'IIIIIIIIIIIIIIIII', i
    content = Contentinfo(name=namestr, absname=namestr, ftype=namestr,
                          superid=namestr,
                          serverid=serverobj, changeflag=namestr,
                          oldproperty=namestr,
                          newproperty=namestr, checkflag=0, writetime=datetime.datetime.now())
    content.save()
