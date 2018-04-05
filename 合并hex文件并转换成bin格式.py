import os
import shutil

AllFile = os.listdir()
DocTimeDict = {}
for FileNameTmp in AllFile:
	DocTimeDict[FileNameTmp] = os.path.getmtime(FileNameTmp)
AllFileName = sorted(DocTimeDict.items(), key = lambda x:x[1])
AllFileNumber = len(AllFile)
print(AllFileNumber)

WriteData = ''
HexToBin = {'0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5':'0101', '6':'0110', '7':'0111', '8':'1000', '9':'1001', 'A':'1010', 'B':'1011', 'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'}
counter = 0
LineNumber = 0
FileNumber = 0
FileCounter = 0

for FileName in AllFileName:
	with open(FileName[0], 'r') as FileRead:
		if FileName[0].split('.')[-1] == 'txt':
			if FileCounter >6500:
				FileCounter = 0
				FileNumber += 1
			print("FileName",FileName[0])
			print(FileCounter,'/',AllFileNumber)
			with open("MH1903_TRNG0_DATA" + str(FileNumber), 'a') as FileWrite:
				FileData = FileRead.readlines()
				for LineData in FileData[1:] :
					counter += 1
					WriteData += HexToBin[LineData[-3:-1][0]]
					WriteData += HexToBin[LineData[-3:-1][1]]
					if counter == 4:
						WriteData += '\n'
						LineNumber += 1
						counter = 0
						if LineNumber % 1000 == 0:
							FileCounter += 1
							FileWrite.write(WriteData)
							WriteData = ''
print("处理完毕。")