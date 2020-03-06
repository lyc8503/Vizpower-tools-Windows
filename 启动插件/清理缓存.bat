@echo off
echo 正在清理缓存
taskkill -f -im explorer.exe
del /f /s /q "%localappdata%\IconCache.db"
del /f /s /q "%localappdata%\Winupon\Vizpower\VPRC"
start explorer.exe
cls
echo 无限宝研究组 1055109700
pause