# os模块是Python标准库中整理文件和目录最为常用的模块，该模块提供了非常丰富的方法用来处理文件和目录
# print("D:/test",r"D:\test","D:\\test") # r使得反斜杠不具备转义作用
import os

# print(os.getcwd()) # 获取当前工作路径

# path=r"D:\study_file\shell-and-python"
# print(os.listdir(path)) # 传入任意一个path路径，返回该路径下所有文件和目录组成的列表
# for path,dirs,files in os.walk(path): # 传入任意一个path路径，深层次遍历指定路径下的所有文件夹，并返回三个变量值，一个是路径、一个是文件夹列表、一个是文件列表
#     print(path)
#     print(dirs)
#     print(files)
#     print("\n")
# print(os.path.exists(path))
# if os.path.exists(path): # 传入任意一个path路径，判断该路径目录或文件是否存在，存在则返回True，反之返回False
#     print("指定目录或文件存在~")
# else:
#     print("指定目录或文件不存在~")
# path1=os.getcwd()+"\\new_dir"
# if os.path.exists(path1):
#     print("指定文件夹存在，无需创建~")
# else:
#     os.mkdir(path1) # 只能创建单层文件夹，不能创建文件
#     print("创建指定文件夹成功~")
# path2=os.getcwd()+"\\new_dir1\\new_dir2"
# if os.path.exists(path2):
#     print("指定递归文件夹存在，无需创建~")
# else:
#     os.makedirs(path2) # 创建递归的文件夹，不能创建文件
#     print("创建指定递归文件夹成功~")
# path3=os.getcwd()+"\\new_dir3"
# if os.path.exists(path3):
#     os.rmdir(path3)  # 只能删除指定的空文件夹，不能删除文件
#     print("删除指定文件夹成功~")
# else:
#     os.mkdir(path3)
#     print("指定文件夹不存在，创建成功~")
# list1=["a.txt","new_dir4"]
# for i in list1:
#     x=os.path.join(path,i) # 路径的拼接
#     print(x)
# path1="D:\study_file\shell-and-python\Test_Project\os_module.py"
# print(os.path.split(path1)) # 传入一个完整的path1路径，将其拆分为绝对路径和文件名组成的元组
# print(os.path.dirname(path1)) # 传入一个完整的path1路径，只返回它的绝对路径
# print(os.path.basename(path1)) # 传入一个完整的path1路径，只返回它的文件名
# path3=os.getcwd()
# file_list=os.listdir(path3)
# print(path3,file_list)
# for file in file_list:
#     if os.path.isdir(file): # 判断是否为文件夹
#         print("文件夹为："+file)
#     if os.path.isfile(file): # 判断是否为文件
#         print("文件："+file)
# path4="D:\study_file\shell-and-python\Test_Project\os_module.py"
# print(os.path.getsize(path4)) # 只能获取文件的大小，以字节为单位

# from os import path
# # file_path=path.join("/var/www","/usr","img","1.jpg") # 会取最后一个绝对路径，即只会保留最后一个绝对路径的值
# # print(file_path)