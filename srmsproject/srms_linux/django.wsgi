import os
import sys
p=os.path.split(os.path.realpath(__file__))[0]
sys.path.append(p)
#sys.stdout = sys.stderr
#print "sys.path==",sys.path
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
os.environ["PYTHON_EGG_CACHE"] = "/tmp"
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler() 

