import random
import os
import sys

file = open("list.txt","rt")
list = file.readlines()
file.close()
list = " ".join(map(str,list))
list = list.split(",")

for element in list:
  element = int(element)

random.shuffle(list)
print(list)
if list != sorted(list):
  os.execv(sys.executable, ['python'] + [__file__])