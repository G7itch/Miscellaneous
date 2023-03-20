import random

file = open("list.txt","rt")
list1 = file.readlines()
file.close()
list1 = " ".join(map(str,list1))
list1 = list1.split(",")

for element in list1:
  element = int(element)

while list1 != sorted(list1):
  chance = random.randint(0,100000000000)
  if chance <= 10:
    b = random.randint(0,len(list1))
    c = random.randint(0,len(list1))
    list1[b],list1[c] = list1[c],list1[b]

print(list1)
