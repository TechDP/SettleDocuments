import os

filename = '200mAh数据处理.txt'
with open(filename,'r') as fr:
    alldata = fr.readlines()
    print(len(alldata))
    with open('200mAh数据处理_done.txt','a') as fw:
    	for linedata in alldata:
    		if linedata[0] != '\n':
    			fw.write(linedata)
