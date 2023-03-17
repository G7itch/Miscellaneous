import random
import os

file = open("list.txt","rt")
list = file.readlines()
file.close()
list = " ".join(map(str,list))
list = list.split(",")

for element in list:
  element = int(element)

listsorted = False
choices = [True,False]
for i in range(8):
  file = open(f"comrade{i}.txt","w")
  file.write(random.choice(choices))
  file.close()

while not(listsorted):
  directory = 'stalin sort'
  for filename in os.listdir(directory):
      if os.path.isfile(f):
        if filename == "list.txt" or filename == "StalinSort.py":
          pass
        else:
          file = open(filename,"rt")
          word = "".join(file.readlines())
          if word == False:
            os.remove(filename)

    ##CHECK IF THEY ARE ALL TRUE, IF THEY ARE CHANGE THE FLAG
        
  