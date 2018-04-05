import random
import os
from struct import *

arrayint = [1,2,3]
print(bytearray(arrayint))
test = 2
print(bytes(hex(2),encoding = 'utf-8'))
print(random.randint(0, 0xF))

filecounter = 16
while filecounter > 0:
	print('creat',filecounter)
	counter = 1024 * 128
	with open('test' + str(filecounter) + '.bin', 'wb') as fbwrite:
		while counter > 0:
			fbwrite.write(pack('B',random.randint(0,0xFF)))
			counter -= 1
		fbwrite.close()
	print('creat',filecounter,'done')
	filecounter -= 1