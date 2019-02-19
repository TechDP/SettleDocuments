#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Let's import what we need
import time
from pywintypes import Time

print(time.time())
print(time.localtime(time.time()))
print(Time(time.localtime(time.time() + 20)))
