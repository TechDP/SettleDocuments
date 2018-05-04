from win32file import CreateFile, SetFileTime, GetFileTime, CloseHandle 
from win32file import GENERIC_READ, GENERIC_WRITE, OPEN_EXISTING
from pywintypes import Time
import time

import sys
import os

# get arguments   
# pfile = "TestModifyProgram.txt"
# cTime = "01.01.2001 00:00:00"
# mTime = "01.01.2001 00:00:00"
# aTime = "01.01.2001 00:00:00"
fName = "test1.bin"

cTime = mTime = aTime = ""

# specify time format
format = "%d.%m.%Y %H:%M:%S"
offset = 0 # in seconds

def is_valid_date(str):
    try:
        time.strptime(str, format)
        return True
    except:
        print("请输入正确时间：")
        return False

# 需要增加输入数据的判断
while False == is_valid_date(cTime):
    gettime_Year = input("输入时间（年份）：")
    if int(gettime_Year) < 1960:
        print("输入时间年份需要大于1960年。")
        continue
    gettime_Mouth = input("输入时间（月份）：")
    getTime_Day = input("输入时间（日期）：")
    getTime_Hour = input("输入时间（小时）：")
    getTime_Minute = input("输入时间（分钟）")
    getTime_Second = input("输入时间（秒）")
    getTime_InterVal = input("输入下一个文件的间隔时间：")
    cTime = mTime = aTime = ("%s.%s.%s %s:%s:%s"%(getTime_Day, gettime_Mouth, gettime_Year, getTime_Hour, getTime_Minute, getTime_Second))


# create struct_time object
# strptime(),转换时间格式的函数
# mktime(),把时间转换成用秒数表示的浮点数
cTime_t = time.localtime(time.mktime(time.strptime(cTime,format))+offset)
mTime_t = time.localtime(time.mktime(time.strptime(mTime,format))+offset)
aTime_t = time.localtime(time.mktime(time.strptime(aTime,format))+offset)
# print("cTime", cTime)
# print("1", cTime_t)

print(time.strptime(cTime, format))
print(time.mktime(time.strptime(cTime, format)))
print(time.localtime(time.mktime(time.strptime(aTime,format))+offset))

# print("2", cTime_t)
# visually check if conversion was ok
print()
print("FileName: %s" % fName)
print("Create  : %s --> %s OK" % (cTime,time.strftime(format,cTime_t)))
print("Modify  : %s --> %s OK" % (mTime,time.strftime(format,mTime_t)))
print("Access  : %s --> %s OK" % (aTime,time.strftime(format,aTime_t)))
print()
# print("3", cTime_t)
# change timestamp of file
fh = CreateFile(fName, GENERIC_READ | GENERIC_WRITE, 0, None, OPEN_EXISTING, 0, 0) 
createTime, accessTime, modifyTime = GetFileTime(fh) 
print("Change Create from",createTime,"to %s" % (time.strftime(format,cTime_t)))
print("Change Modify from",modifyTime,"to %s" % (time.strftime(format,mTime_t)))
print("Change Access from",accessTime,"to %s" % (time.strftime(format,aTime_t)))
print()
# print("4", cTime_t)
print(createTime)
createTime = Time(time.mktime(cTime_t))
accessTime   = Time(time.mktime(aTime_t))
modifyTime    = Time(time.mktime(mTime_t))
print(createTime, accessTime, modifyTime)
SetFileTime(fh, createTime, accessTime, modifyTime) 
CloseHandle(fh)

# check if all was ok
ctime = time.strftime(format,time.localtime(os.path.getctime(fName)))
mtime = time.strftime(format,time.localtime(os.path.getmtime(fName)))
atime = time.strftime(format,time.localtime(os.path.getatime(fName)))

print("CHECK MODIFICATION:")
print("FileName: %s" % fName)
print("Create  : %s" % (ctime))
print("Modify  : %s" % (mtime))
print("Access  : %s" % (atime))