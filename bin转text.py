counter = 0
fileName = input("输入要转换的文件名称")
with open(fileName + ".txt", 'w') as fileWrite:
    with open(fileName, 'rb') as fileRead:
        data = fileRead.read(1)
        while data:
            if counter == 16:
                fileWrite.write("\n")
                counter
            writedata = bytearray(data).hex()
            fileWrite.write('0x' + writedata + ",")
            counter += 1
            data = fileRead.read(1)

