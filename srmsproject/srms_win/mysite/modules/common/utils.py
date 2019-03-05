# coding=utf-8
import traceback
from modules.contentinfo.models import Contentinfo
from modules.serverinfo.models import Serverinfo
from mysite import settings
import os
import zipfile

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


#上传文件
def uploadfile(request, requestfname, fname):
    try:
        os.makedirs(os.path.split(fname)[0])
    except:
        pass
    f = request.FILES[requestfname]
    file = open(fname, 'wb+')
    for chunk in f.chunks():
        file.write(chunk)
    file.close()


def unzipFile(source_file, target_dir):
    fl = {}
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    if target_dir[-1] not in ["/", "\\"]:
        target_dir += "/"
    z = zipfile.ZipFile(source_file, 'r')
    for fn in z.namelist():
        bytes = z.read(fn)
        filename = target_dir + fn
        #		print filename
        if (len(bytes) == 0) and (fn[-1] in ["/", "\\"]):
            try:
                os.makedirs(filename)
            except:
                pass
        else:
            try:
                os.makedirs("/".join(filename.split('/')[:-1]))
            except:
                pass
            file(filename, "wb+").write(bytes)
            fl[filename] = len(bytes)
    return fl


#文件升级
def updatefile(request, requestfname, fname):
    pass


#目录升级
def updatedir(request, requestfname, fname):
    pass


#系统升级
def updatesys(request):
    fname = "update.zip"
    source_file = "%s%s%s" % (settings.ADDITION_FILE_ROOT, 'upload/system/update/', fname)
    target_dir = "%s" % (settings.BASE_DIR)
    unzipFile(source_file, target_dir)
