###########################################
## This is pracricing manipulating files ##
###########################################

import os
import time


path1 = "/"

dir_list1 = os.listdir(path1)

for i in dir_list1:
    print(i)


path2 = "/home"
print(os.path.join(path2, "devins/Desktop", "testfile.txt"))

path3 = "/home/devins/Desktop/testfile.txt"
mod_time1 = os.path.getmtime(path3)
local_time1 = time.ctime(mod_time1)

print("The last time the file was modified was {}".format(local_time1))

path4 = "/home/devins/Desktop/os_script"
dir_list2 = os.listdir(path4)
mod_time2 = os.path.getmtime(path4)
local_time2 = time.ctime(mod_time2)

for x in dir_list2:
    if x.endswith(".txt"):
        print("File Name: {} -- Mod Time: {}".format(x, local_time2))