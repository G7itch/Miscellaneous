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

for i in range(len(list1)-1):
  sortedlist = sorted(list1[:i]) + list1[i:]
  print(sortedlist)

print(sortedlist)
