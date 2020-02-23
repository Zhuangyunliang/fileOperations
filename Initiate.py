from Clean import deldisk
from Categorize import categorize
import sys
#Categorize.Categorize();
def welcome():#欢迎界面
    print("********************************************")
    print("*          欢迎使用工具箱v1.0          *")
    print("*                                          *")
    print("* 1.重复文件清理  2.文件分类  3.关闭工具箱 *")
    print("*                                          *")
    print("*          更多功能正在赶来的路上!         *")
    print("********************************************")
    #str = input("请输入你想要使用功能前的数字：")
def go():
    flag = input("执行完成！是否继续使用本工具箱? 是/否")
    if flag == "是":
        welcome()
    else:
        sys.exit(0) #参数0为正常退出 1为异常退出
welcome()
str = input("请输入你想要使用功能前的数字：")
while 1:
    if str == "1":
        deldisk();
        go()
        str = input("请输入你想要使用功能前的数字：")
    elif str == "2":
        categorize()
        go()
        str = input("请输入你想要使用功能前的数字：")
    elif str == "3":
        sys.exit()
        print("再见！欢迎下次使用。")
    else:
        str = input("非法字符！请输入你想要使用功能前的数字：")




