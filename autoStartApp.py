'''
@Author: SaiyanmanJ
@Date: 2020-07-28 11:41:11
@LastEditors: SaiyanmanJ
@LastEditTime: 2020-07-28 15:37:23
@FilePath: \automate-start-app\autoStartApp.py
@Description: app gui
'''

import function 
import tkinter as tk
import time

# 开机自启动后多久启动app
delay_time = 1

time.sleep(delay_time)

function.start_app()

# 设置窗口属性
window = tk.Tk()
window.title("automate start app settings")
window.geometry('400x400')

# label 提示
var = tk.StringVar()
label = tk.Label(window, textvariable = var,bg = 'green', width = 100, height = 2)
label.pack()

# 输入框
entry = tk.Entry(window,show=None,width = 100)
entry.pack()

# listbox 展示程序名称
lb = tk.Listbox(window)
# 展示app信息
def show_app():
    lb.delete(0, "end")
    for app_name in function.get_app_name():
        lb.insert("end", app_name)
# 删除app信息
def delete_app():
    app_name = lb.get(lb.curselection()) # 获取鼠标选中的文本
    lb.delete(lb.curselection()) # 删除 listbox 中的文本
    function.delete_app_path(app_name) # 删除 app_path.json 中的文本

show_app()
lb.pack()



# 添加路径
def add_path():
    path = entry.get()
    if len(path) > 0:
        if function.add_app_path(path):
            var.set("path has added") # 设置 label 提示
            entry.delete(0,200) # 清空 entry 的值
            show_app() # 更新app信息
        else:
            var.set("error, please check path")
    else:
        var.set("please input path")
    

# 添加按钮
add_button = tk.Button(window, text = 'add', width = 15, height = 2, command = add_path)
add_button.pack()
# 删除按钮
del_button = tk.Button(window, text = 'delete', width = 15, height = 2, command=delete_app)
del_button.pack()


window.mainloop()