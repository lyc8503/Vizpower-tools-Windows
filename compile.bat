pyinstaller -F copy.py
rmdir __pycache__ /Q /S
rmdir build /Q /S
copy .\dist\copy.exe .\ /Y
rmdir dist /Q /S
del copy.spec /Q /F /S
pause