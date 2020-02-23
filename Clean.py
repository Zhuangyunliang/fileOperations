import sys
import hashlib
import os
import psutil#读取计算机硬件的类库
def getHash(f):   #返回16位的哈希数值
    line =f.readline()
    md5 = hashlib.md5()
    while(line):
        md5.update(line)
        line = f.readline()
    return md5.hexdigest()
def isHashEqual(f1,f2): #对比HASH是否相同
    str1 = getHash(f1)
    str2 = getHash(f2)
    return str1 == str2
#path1 =open("E:\\1\\5.txt","rb")#rb使用二进制进行只读操作
#path2 =open( "E:\\1\\1\\2.txt","rb")
#print(isHashEqual(path1,path2))
#print(os.path.split("E:\\1\\1\\2.txt")[1])
def getAbsroute(rootdir):  # path文件路径  allfile为存放文件路径（包含文件名）的列表
    allfile = []
    filename = os.listdir(rootdir)
    # print(filename)
    for i in range(0,len(filename)):
        path = os.path.join(rootdir,filename[i])
        if os.path.isdir(path):
            #出现访问文件夹权限不足的异常
            try:
                allfile.extend(getAbsroute(path))
            except:
                pass
        if os.path.isfile(path):
            allfile.append(path)
    #print(allfile)
    return allfile
# str = input("请输入盘符：")
#filelist = getAbsroute(str)
#print(filelist)
def clean_welcome():
    print("********************************************")
    print("*            重复文件清理工具v1.0          *")
    print("*                                          *")
    print("* 1.全盘清理 2.除c盘全部清理 3.指定盘符清理*")
    print("*            4.指定文件夹清理             *")
    print("*          更多功能正在赶来的路上!         *")
    print("********************************************")
#获取计算机硬盘号
def findDisk():
    disklist =[]
    disks = psutil.disk_partitions()
    #print(disks)
    for disk in disks:
        disklist.append(disk[0])
    return  disklist
#path = "E:/working"
def delFile(filelist):
    #filelist = getAbsroute(path)
    lenght = len(filelist)
    for i in range(lenght):
        for j in range(i+1,lenght):
            #if os.path.exists(filelist[i]) and os.path.exists(filelist[j]):
            try:
                path1 = open(filelist[i], "rb")  # rb使用二进制进行只读操作
                path2 = open(filelist[j], "rb")
            except:
                continue
            # print(os.path.split(filelist[i])[1])
            # print(os.path.split(filelist[j])[1])
            if isHashEqual(path1,path2) and (os.path.split(filelist[i])[1] == os.path.split(filelist[j])[1]):
                path1.close()
                path2.close()
                # print(filelist[i])
                # print(filelist[j])
                # print(len(filelist[i]) < len(filelist[j]))
                if(len(filelist[i]) <= len(filelist[j])):
                    try:
                        os.remove(filelist[j])
                        print(filelist[j] + "已经被删除")
                        print(filelist[i] + "被保留")
                        ph = str(os.path.split(filelist[j])[0])
                        if(os.listdir(ph) == []):
                            os.removedirs(ph)
                    except Exception as e:
                        print(e)
                else:
                    try:
                        os.remove(filelist[i])
                        print(filelist[i] + "已经被删除")
                        print(filelist[j] + "被保留")
                        ph = str(os.path.split(filelist[i])[0])
                        if (os.listdir(ph) == []):
                            os.removedirs(ph)
                    except Exception as e:
                        print(e)
    print("清理完成！")
#delFile(path)
def go():
    flag = input("执行完成！是否继续使用清理功能? 是/否")
    if flag == "是":
        clean_welcome()
    else:
        sys.exit(0) #参数0为正常退出 1为异常退出

#需要清理的盘符
def clean_disks(disklist):
    filelist = []
    for disk in disklist:
        filelist.extend(getAbsroute(disk))
    delFile(filelist)
def deldisk():
    print()
    print()
    print()
    clean_welcome()
    str = input("请输入你想要使用功能前的数字：")
    while 1:
        if str == "1":
            disklist = findDisk()
            clean_disks(disklist)
            go()
            str = input("请输入你想要使用功能前的数字：")
        elif str == "2":
            disklist = findDisk()
            #print(disklist)
            disklist.remove("C:\\")
            clean_disks(disklist)
            go()
            str = input("请输入你想要使用功能前的数字：")
        elif str == "3":
            print("请选择你想要清理的磁盘名：")
            disklist = findDisk();
            disks = {}
            for i in range(len(disklist)):
                str_i = chr(49+i)
                disks[str_i] = disklist[i]
                str1 = str_i+". 本地磁盘"+disklist[i][0:1]
                print(str1,end='\t')
            print()
            #print(disks)
            disklist_clean = []
            str = input("请输入你想要使用功能前的数字,用空格隔开：")
            #print(str)
            # while(1):
            #     if str != '\n':
            #         disklist_clean.append(disks[str])
            #     else:
            #         break
            # print(disklist_clean)
            disklist_clean = str.split(' ')
            for index in range(len(disklist_clean)):
                disklist_clean[index] = disks[disklist_clean[index]]
            print(disklist_clean)
            clean_disks(disklist_clean)
            go()
        elif str == "4":
            str = input("请输入指定文件夹路径(若有多个请用空格隔开)：")
            disklist_clean = str.split(' ')
            clean_disks(disklist_clean)
            go()
            str = input("请输入你想要使用功能前的数字：")
        else:
            str = input("非法字符！请输入你想要使用功能前的数字：")