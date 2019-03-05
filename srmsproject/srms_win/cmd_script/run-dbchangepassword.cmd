
cls
@echo off
call init.bat

python ..\mysite\manage.py  changepassword admin

pause

