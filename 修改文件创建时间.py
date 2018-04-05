import os.path, time, os

# class TypeError (Exception):
# 	pass

# if __name__ == '__main__':
# 	if (len(os.sys.argv) < 1):
# 		raise TypeError()
# 	else:
# 		print("os.sys.argv[0]: %s" % os.sys.argv[0])
#    # os.sys.argv[0] is the current file, in this case, file_ctime.py
# 	f = os.sys.argv[0]
# 	mtime = time.ctime(os.path.getmtime(f))
# 	ctime = time.ctime(os.path.getctime(f))
# 	print("Last modified : %s, last created time: %s" % (mtime, ctime))
filename = 'testchangecreattime.txt'
mtime = time.ctime(os.path.getmtime(filename))
ctime = time.ctime(os.path.getctime(filename))
print(mtime)
print(ctime)
print(os.path.getmtime(filename))
print(os.path.getctime(filename))
os.utime(filename,(1522843651.1382766, 1522843651.1382766))
mtime = time.ctime(os.path.getmtime(filename))
ctime = time.ctime(os.path.getctime(filename))
print(mtime)
print(ctime)
print(os.path.getmtime(filename))
print(os.path.getctime(filename))
# Help on built-in function utime in module posix:
# while True:
# 	pass
# utime(...)
#     utime(path, (atime, mtime))
#     utime(path, None)

#     Set the access and modified time of the file to the given values.  If the
#     second form is used, set the access and modified times to the current time.