import os

filename = input("输入文件完整名称，带后缀：")
with open("result.txt", 'w') as writeFile:
    with open(filename, 'r') as readFile:
        for i in readFile.readlines():
            
            counter = 0
            linesize = 0
            if i[-1] == '\n':
                linesize = len(i) - 1
                if len(i) >= 2:
                    if i[-2] == ':':
                        writeFile.write(i)
                        continue
            else:
                linesize = len(i)
            while counter < linesize:
                # print(i[counter:counter + 2])
                writeFile.write('0x'+ i[counter:counter + 2] + ', ')
                counter += 2
            writeFile.write('\n')
