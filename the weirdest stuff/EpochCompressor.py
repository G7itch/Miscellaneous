from datetime import datetime, timedelta

epoch = ""
filename = input("enter file to open: ")
file = open(filename,"rt")
content = file.readlines()
file.close()

for line in content:
    for word in line:
        for letter in word:
            epoch+=str(ord(letter))


print("The epoch is:")
epoch = list(epoch)
newepoch = ""
for i in range(0,len(epoch)-2):
    a = int(epoch[i])
    b = int(epoch[i+1])
    newepoch += str(int((0.5*(a+b)*(a+b+1))+b))


##########THISDOESNT WORK COZ IM TRYING TO MAP A LARGE NUMBER TO A SMALL NUMBER
##########WITOUT LOSING PRECISION WHICH IS IMPOSSIBLE
