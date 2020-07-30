<!--
 * @Author: SaiyanmanJ
 * @Date: 2020-07-28 11:40:48
 * @LastEditors: SaiyanmanJ
 * @LastEditTime: 2020-07-31 00:00:11
 * @FilePath: \automate-start-app\README.md
 * @Description: 
--> 
# automate-start-app
now, just test on windows

## 状态
使用 pyinstaller 打包成exe，设置自启动可能会出现无法运行的错误，还未解决
下一步：考虑用复选框选择自启动的app，当前只能全部自启动，不能选择

## 设置自启动
* 1.进入程序根目录找到 autoStartApp.exe 可执行文件
* 2.为autoStartApp.exe 创建快捷方式
* 3.将快捷方式复制到 C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp 目录下
## 功能
* 增加，删除 app
* 检测 app 路径是否合法
* 设置自启动后开机自启动app
## 注意
* app启动间隔设置为3秒，接连启动大型程序可能会卡顿