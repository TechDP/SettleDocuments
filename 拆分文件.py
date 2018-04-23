import sys,os

kilobytes = 1024
megabytes = kilobytes*1000
chunksize = int(128*megabytes)#default chunksize

def split(fromfile,todir,chunksize=chunksize):
    # 判断是否已经存在文件夹，如果存在，则清空文件夹里的内容
    if not os.path.exists(todir):#check whether todir exists or not
        os.mkdir(todir)          
    else:
        for fname in os.listdir(todir):
            os.remove(os.path.join(todir,fname))
    partnum = 0
    inputfile = open(fromfile,'rb')#open the fromfile
    while True:
        chunk = inputfile.read(chunksize)
        if not chunk:             #check the chunk is empty
            break
        partnum += 1
        filename = os.path.join(todir,('part%04d'%partnum))
        fileobj = open(filename,'wb')#make partfile
        fileobj.write(chunk)         #write data into partfile
        fileobj.close()
    return partnum
if __name__=='__main__':
        fromfile  = input('要拆分文件名？')
        todir     = input('拆分后存放目录名？')
        chunksize = int(input('拆分的每个文件大小？单位Mb'))
        chunksize = chunksize * 1024 * 1024
        # map(function, iterable, ...) 
        # 第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
        # os.path.abspath 返回一个目录的绝对路径
        absfrom,absto = map(os.path.abspath,[fromfile,todir])
        print('Splitting',absfrom,'to',absto,'by',chunksize)
        try:
            parts = split(fromfile,todir,chunksize)
        except:
            print('Error during split:')
            print(sys.exc_info()[0],sys.exc_info()[1])
        else:
            print('split finished:',parts,'parts are in',absto)