#Suduko editor
filename = input("Enter filename: ")
file = open(filename,"rt")
content = [line.rstrip('\n') for line in file]
file.close()



for line in content:
    if len(set(line)) != len(line):
        raise Exception("breaks shizzle")

for ind,line in enumerate(content):
    content[ind] = line.split(" ")

