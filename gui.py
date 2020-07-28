'''
@Author: SaiyanmanJ
@Date: 2020-07-28 09:32:41
@LastEditTime: 2020-07-28 11:26:39
@LastEditors: Please set LastEditors
@Description: GUI
@FilePath: \automate_start_app\gui.py
'''
from AutomateStart import add_app_path, get_app_path, start_app, start_interval
import tkinter as tk






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

# 添加路径
def add_path():
    path = entry.get()
    if add_app_path(path):
        var.set("path has added") # 设置 label 提示
        entry.delete(0,200) # 清空 entry 的值
    else:
        var.set("error, please check path")
    
# 文本框
text = tk.Text(window, height = 10)
text.pack()



# 添加按钮
add_button = tk.Button(window, text = 'add', width = 15, height = 2, command = add_path)
add_button.pack()
# 删除按钮
del_button = tk.Button(window, text = 'delete', width = 15, height = 2)
del_button.pack()





window.mainloop()