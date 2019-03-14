import sys,os
import time
from struct import *

def split(fromfile,todir):
    # 判断是否已经存在文件夹，如果存在，则清空文件夹里的内容
    if not os.path.exists(todir):#check whether todir exists or not
        os.mkdir(todir)          
    else:
        for fname in os.listdir(todir):
            os.remove(os.path.join(todir,fname))
    fileSize = os.path.getsize(fromfile)
    if fileSize < (64 * 1024):
        print("文件大小小于64K")
        return False
    with open(fromfile,'rb') as inputfile:
        chunk = inputfile.read(fileSize - (64 * 1024))
        chunk = inputfile.read(64 * 1024)
        filename = os.path.join(todir,(os.path.splitext(fromfile)[0] + "result" + os.path.splitext(fromfile)[1]))
        with open(filename,'wb') as FileWrite:
            counter = 0
            while counter < (1024 - 64) * 1024:
                FileWrite.write(pack('B',0xFF))
                counter += 1
            FileWrite.write(chunk)

if __name__=='__main__':
        fromfile  = input('要更改的文件名？')
        time = time.localtime(time.time())
        todir = str(time.tm_year) + "_" + str(time.tm_mon) + "_" + str(time.tm_mday) + "_" + str(time.tm_hour) + "_" + str(time.tm_min) + "_" + str(time.tm_sec)

        # map(function, iterable, ...) 
        # 第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
        # os.path.abspath 返回一个目录的绝对路径
        try:
            split(fromfile,todir)
        except:
            print('Error during split:')
            print(sys.exc_info()[0],sys.exc_info()[1])
        else:
            print('split finished。')