import random

file = open("list.txt","rt")
list = file.readlines()
file.close()
list = " ".join(map(str,list))
list = list.split(",")

for element in list:
  element = int(element)

while list != sorted(list):
  chance = random.randint(0,100000000000)
  if chance <= 10:
    b = random.randint(0,len(list))
    c = random.randint(0,len(list))
    list[b],list[c] = list[c],list[b]

