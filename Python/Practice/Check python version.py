#using sys module
import sys

print("Python version:")
print(sys.version) #output: 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)]
print("Version info:")
print(sys.version_info) #output: sys.version_info(major=3, minor=12, micro=4, releaselevel='final', serial=0)

#using platform module

import platform

print(platform.python_version()) #output: 3.12.4
print(platform.python_version_tuple()) #output: ('3', '12', '4')





