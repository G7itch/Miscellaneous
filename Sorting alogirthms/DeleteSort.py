file = open("list.txt","rt")
list1 = file.readlines()
file.close()
list1 = " ".join(map(str,list1))
list1 = list1.split(",")

for element in list1:
  element = int(element)
  
while list1 != sorted(list1):
  list1 = list1[1:]
  
print(list1)
