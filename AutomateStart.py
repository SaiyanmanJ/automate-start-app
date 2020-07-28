'''
@Author: SaiyanmanJ
@Date: 2020-07-27 17:20:18
@LastEditTime: 2020-07-28 11:11:36
@LastEditors: Please set LastEditors
@Description: automate start app
@FilePath: \automate_start_app\AutomateStart.py
'''
import subprocess
import json
import time
import psutil
import tkinter
from pathlib import Path

# 程序启动间隔单位秒
start_interval = 1

# 判断进程是否在运行函数
def process_exist(process_name):
    pids = psutil.pids()
    for pid in pids:
        if psutil.Process(pid).name() == process_name:
            return True
    return False

# 添加日志信息函数
def add_log(info):
    with open('log.txt', 'a') as log:
        log.write(info + " " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "\n")

def add_app_path(path):

    # 查看路径是否存在
    if not Path(path).exists():
        return False
        
    # 读取文件数据
    jsonData = json.load(open('app_path.json','r'))
    
    with open('app_path.json', 'w', encoding='utf8') as f:
        name_begin = path.rfind("\\")
        
        if name_begin != -1:
            app_name = path[name_begin + 1:]
        else:
            app_name = path[path.rfind("/") + 1:]    
    
        if len(app_name) > 0:
            jsonData[app_name] = path # 添加路径信息
            json.dump(jsonData, f) # 写入数据
            return True
        
    return False
            
def get_app_path():
    with open('app_path.json', 'r', encoding='utf8') as f:
        jsonData = json.load(f)
        return jsonData        

# 打开程序路径信息文件，启动程序
def start_app():
    with open('app_path.json', 'r', encoding='utf8') as f:
        jsonData = json.load(f)
        for k, v in jsonData.items():
            time.sleep(start_interval) # 推迟执行 单位秒
            if process_exist(k): # 判断程序是否已经启动
                add_log(k + " is runing")
            else:
                try:
                    subprocess.Popen(v) # 启动程序
                except FileNotFoundError: # 路径错误，文件不存在
                    add_log(k + " is not found")


