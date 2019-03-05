
cls
@echo off
call init.bat


python del_db_initials.py
pause
python ..\mysite\manage.py  makemigrations
pause
python ..\mysite\manage.py  migrate
pause
