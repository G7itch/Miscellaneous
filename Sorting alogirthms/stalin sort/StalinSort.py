import random
import os

file = open("list.txt","rt")
lista = file.readlines()
file.close()
lista = " ".join(map(str,lista))
lista = lista.split(",")

for element in lista:
  element = int(element)

listsorted = False
choices = [True,False]
for i in range(8):
  file = open(f"comrade{i}.txt","w")
  file.write(str(random.choice(choices)))
  file.close()

numagree = 0
while not(listsorted):
  directory = '.'
  for filename in os.listdir(directory):
      if os.path.isfile(filename):
        if filename == "list.txt" or filename == "StalinSort.py":
          pass
        else:
          file = open(filename,"rt")
          word = "".join(file.readlines())
          if word == "False":
            os.remove(filename)
          else:
            numagree += 1
  if numagree == len(os.listdir(directory))-2:
    print(lista)
    listsorted = True
    ##CHECK IF THEY ARE ALL TRUE, IF THEY ARE CHANGE THE FLAG
        
  
