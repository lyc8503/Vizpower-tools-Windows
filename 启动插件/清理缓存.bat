@echo off
echo ����������
taskkill -f -im explorer.exe
del /f /s /q "%localappdata%\IconCache.db"
del /f /s /q "%localappdata%\Winupon\Vizpower\VPRC"
start explorer.exe
cls
echo ���ޱ��о��� 1055109700
pause