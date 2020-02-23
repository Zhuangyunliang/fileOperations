import os
import shutil


def readFilename(path, allfile):  # path文件路径  allfile为存放文件路径（包含文件名）的列表
    filelist = os.listdir(path)  # 返回path指定的文件夹包含的文件或文件夹的名字的列表
    print(filelist)
    for filename in filelist:
        filepath = os.path.join(path, filename)  # 将path和filename拼接获得文件的绝对路径
        if os.path.isdir(filepath):# 如果是一个文件夹

            readFilename(filepath, allfile)
        else:
            allfile.append(filepath)
    return allfile


def mycopyfile(srcfile, dstfile):  # srcfile源文件  dstfile目标文件
    if not os.path.isfile(srcfile):
        print("%s not exist!" % (srcfile))
    else:
        fpath, fname = os.path.split(dstfile)  # 分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)  # 创建路径
        shutil.copyfile(srcfile, dstfile)  # 复制文件
        print("copy %s -> %s" % (srcfile, dstfile))


def categorize():
    path1 = input("请输入需要整理的文件夹路径：")
    while 1:
        if path1 !="":
            break
        else:
            path1 = input("请输入需要整理的文件夹路径：")
    allfile1 = []  # 存放所有文件路径的列表
    allfile1 = readFilename(path1, allfile1)  # 将path1路径下的所有文件名都放在allfile1列表中
    path2 = input("请输入需要整理文件那个文件夹：")
    for srcfile in allfile1:
        #print(path1)
        file111 = os.path.split(srcfile)[1] #file111为文件名+文件格式
        #print(file111)
        type = os.path.splitext(srcfile)[1]#获取文件类型
        dstfile = path2 + "\\"+type.split('.')[-1] +"\\"+ file111
        #print(dstfile)
        mycopyfile(srcfile, dstfile)

        print("整理完成！")
