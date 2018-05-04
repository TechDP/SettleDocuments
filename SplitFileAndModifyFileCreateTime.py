import sys, os, time, win32timezone
from win32file import CreateFile, SetFileTime, GetFileTime, CloseHandle 
from win32file import GENERIC_READ, GENERIC_WRITE, OPEN_EXISTING
from pywintypes import Time

format = "%d.%m.%Y %H:%M:%S"

def modifyFileTime(filename, filetime, offsettime):
    createTime = accessTime = modifyTime = Time(time.localtime(time.mktime(time.strptime(filetime,format)) + offsettime))
    fh = CreateFile(filename, GENERIC_READ | GENERIC_WRITE, 0, None, OPEN_EXISTING, 0, 0) 
    SetFileTime(fh, createTime, accessTime, modifyTime) 
    CloseHandle(fh)

def is_valid_date(str):
    try:
        time.strptime(str, format)
        return True
    except:
        print("请输入正确时间：")
        return False

def splitfile(fromfile, SplitFileName, chunksize, filetime, InterVal):
    # 判断是否已经存在文件夹，如果存在，则清空文件夹里的内容
    todir = "data"
    if not os.path.exists(todir):#check whether todir exists or not
        os.mkdir(todir)          
    else:
        for fname in os.listdir(todir):
            os.remove(os.path.join(todir,fname))
    partnum = 0
    inputfile = open(fromfile,'rb')#open the fromfile
    offsettime = 0
    while True:
        chunk = inputfile.read(chunksize)
        if not chunk:             #check the chunk is empty
            break
        
        filename = os.path.join(todir,(SplitFileName + '%03d'%partnum + ".dat"))
        fileobj = open(filename,'wb')#make partfile
        fileobj.write(chunk)         #write data into partfile
        fileobj.close()
        modifyFileTime(filename, filetime, offsettime)
        partnum += 1
        offsettime += InterVal
    return partnum

if __name__=='__main__':
    cTime = ""
    getfilename = ""
    while not os.path.exists(getfilename):
        getfilename  = input('要拆分文件名？')
        if not os.path.exists(getfilename):
            print(getfilename + "文件不存在")
    getSplitFileName_1 = input("拆分后文件命名的温度？")
    getSplitFileName_2 = input("拆分后文件命名的频率？")
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
        getTime_InterVal = int(input("输入下一个文件的间隔时间："))
        cTime = mTime = aTime = ("%s.%s.%s %s:%s:%s"%(getTime_Day, gettime_Mouth, gettime_Year, getTime_Hour, getTime_Minute, getTime_Second))
    SplitFileName = str(getSplitFileName_1) + '_' + str(getSplitFileName_2) + '_' + str(gettime_Mouth) + '_' + str(getTime_Day) + '_' + str(getTime_Hour) + '_' + str(getTime_Minute) + '_'
    splitfile(getfilename, SplitFileName, 128 * 1024, cTime, getTime_InterVal)
    # getfilename = "testreadwrite.bin"
    # gettime_Year = 1985
    # gettime_Mouth = 5
    # getTime_Day = 1
    # getTime_Hour = 2
    # getTime_Minute = 3
    # getTime_Second = 4
    # getTime_InterVal = 20
    # getSplitFileName_1 = "-20"
    # getSplitFileName_2 = "76MHz"
    # cTime = mTime = aTime = ("%s.%s.%s %s:%s:%s"%(getTime_Day, gettime_Mouth, gettime_Year, getTime_Hour, getTime_Minute, getTime_Second))
    # SplitFileName = str(getSplitFileName_1) + '_' + str(getSplitFileName_2) + '_' + str(gettime_Mouth) + '_' + str(getTime_Day) + '_' + str(getTime_Hour) + '_' + str(getTime_Minute) + '_'
    # splitfile(getfilename, SplitFileName, 128 * 1024, cTime, getTime_InterVal)
    