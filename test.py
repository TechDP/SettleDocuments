import time
from pywintypes import Time

print(time.time())
print(time.localtime(time.time()))
print(Time(time.localtime(time.time() + 20)))