import os
from shutil import copy
import sys


os.chdir(".\\wxbhook-latest")

possible_locations = [
    "C:\\Program Files\\wxb\\",
    "C:\\Program Files (x86)\\wxb\\",
    "D:\\Program Files\\wxb\\",
    "D:\\Program Files (x86)\\wxb\\",
    "E:\\Program Files\\wxb\\",
    "E:\\Program Files (x86)\\wxb\\",
    "F:\\Program Files\\wxb\\",
    "F:\\Program Files (x86)\\wxb\\",
]


wxb_path = None

for loc in possible_locations:
    if os.path.exists(loc + "iMeeting.exe"):
        wxb_path = loc
        break
else:
    print("未在标准安装目录下找到无限宝程序...请手动安装.")
    input("")
    sys.exit(1)

print("正在复制文件...")
for file_name in os.listdir("."):
    try:
        copy(file_name, wxb_path)
    except Exception as e:
        print("出错: " + str(e))

print("清理缓存...")
os.system(".\\..\\clean.bat")
input("安装成功完成!")
