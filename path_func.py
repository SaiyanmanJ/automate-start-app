'''
@Author: SaiyanmanJ
@Date: 2020-07-28 11:41:11
@LastEditors: SaiyanmanJ
@LastEditTime: 2020-07-28 18:10:55
@FilePath: \automate-start-app\path_func.py
@Description: 添加文件的程序
'''

import subprocess
import json
import time
import psutil
import tkinter
from pathlib import Path



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

# 添加 app 路径
def add_app_path(path):

    # 查看路径是否存在 
    if not Path(path).exists():
        return False
        
    # 读取文件数据
    jsonData = json.load(open('app_path.json','r'))
    
    with open('app_path.json', 'w', encoding='utf8') as f:
        name_begin = path.rfind("\\")
        
        if name_begin != -1:
            app_name = path[name_begin + 1: path.rfind(".")]
        else:
            app_name = path[path.rfind("/") + 1: path.rfind(".")]    
    
        if len(app_name) > 0:
            jsonData[app_name] = path # 添加路径信息
            json.dump(jsonData, f) # 写入数据
            return True
        
    return False
            
# 返回程序的名称
def get_app_name():
    with open('app_path.json', 'r', encoding='utf8') as f:
        jsonData = json.load(f)

        app_name = []
        for k, v in jsonData.items():
            app_name.append(k)
        return app_name 

# 返回app路径
def get_app_path(app_name):
    with open('app_path.json', 'r', encoding='utf8') as f:
        jsonData = json.load(f)

        for k, v in jsonData.items():
            if k == app_name:
                return v
    return "" 
# 删除 app 信息
def delete_app_path(app_name):

    jsonData = json.load(open('app_path.json','r'))
    
    with open('app_path.json', 'w', encoding='utf8') as f:
        if app_name in jsonData:
            del jsonData[app_name]
            json.dump(jsonData, f)
            return True
    return False

# 程序启动间隔单位秒
start_interval = 3

# 打开程序路径信息文件，启动程序
def start_app():
    with open('app_path.json', 'r', encoding='utf8') as f:
        jsonData = json.load(f)
        for k, v in jsonData.items():
            time.sleep(start_interval) # 推迟执行 单位秒
            if process_exist(k + ".exe"): # 判断程序是否已经启动
                add_log(k + " is runing")
            else:
                try:
                    subprocess.Popen(v) # 启动程序
                except FileNotFoundError: # 路径错误，文件不存在
                    add_log(k + " is not found")
     
#-------------------------------------------------------------
# 暂时无用

# 将需要自启动的app加入到 auto_start_app.json 中
def add_auto_start_app(app_name):
    
    # 读取文件数据
    jsonData = json.load(open('auto_start_app.json','r'))
    # 获取app路径
    path = get_app_path(app_name)

    # 写回文件
    with open('app_start_app.json', 'w', encoding='utf8') as f:
        
        if len(app_name) > 0:
            jsonData[app_name] = path # 添加路径信息
            json.dump(jsonData, f) # 写入数据
            return True
    return False

# 删除 自启动app
def delete_auto_start_app(app_name):
    jsonData = json.load(open('auto_start_app.json','r'))
    
    with open('auto_start_app.json', 'w', encoding='utf8') as f:
        if app_name in jsonData:
            del jsonData[app_name]
            json.dump(jsonData, f)
            return True
    return False

