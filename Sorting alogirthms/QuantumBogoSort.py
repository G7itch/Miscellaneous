
import random
import os
import sys

file = open("list.txt","rt")
list1 = file.readlines()
file.close()
list1 = " ".join(map(str,list1))
list1 = list1.split(",")

for element in list1:
  element = int(element)

random.shuffle(list1)
print(list1)
if list != sorted(list1):
  os.execv(sys.executable, ['python'] + [__file__])
