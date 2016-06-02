import glob, os
import time
from os import path

list= []
# Open a file
path = "C:\\pet_projects\\try"
dirs = os.listdir( path )

# This would print all the files and directories
for file in dirs:
    list.append(time.ctime(os.stat(path + "\\" + file).st_atime))
list.sort()
print(list)
print(file + list[0])
# os.chdir('C:\pet_projects\Series-Restore')
# for file in glob.glob("*.py"):
#     print(file)
# print("asdf")

# os.chdir('C:\\Users\\vishnu.g\\Recent')
# for file in glob.glob("*.lnk"):
#     print(file)
# print("asdf")

# list.append(time.ctime(os.stat("C:\\pet_projects\\youtube-dl\\youtube.py").st_atime))
# list.append(time.ctime(os.stat("C:\\pet_projects\\sub\\abc.py").st_atime))
# # print((time.ctime(os.stat("C:\\pet_projects\\sub\\abc.py").st_atime))[-13:])
# print(list)
# list.sort()
# print(list)