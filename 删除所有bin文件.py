import os

AllFile = os.listdir()
DocTimeDict = {}
for FileNameTmp in AllFile:
    DocTimeDict[FileNameTmp] = os.path.getmtime(FileNameTmp)
AllFileName = sorted(DocTimeDict.items(), key = lambda x:x[1])
AllFileNumber = len(AllFile)
print(AllFileNumber)
print(AllFileName)

for FileName in AllFileName:
    if FileName[0].split('.')[-1] == 'bin':
        print("删除文件：%s"%FileName[0])
        os.remove(FileName[0])
print("删除完毕")        
