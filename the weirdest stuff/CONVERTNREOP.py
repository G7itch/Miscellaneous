file = open("newoperator.py","rt")
content = file.readlines()
file.close()

class sup(object):

    def __init__(self):
        self.values = []

    def setvalue(self,value):
        self.values.append(value)

    def __eq__(self,other):
        for ele in self.values:
            if ele == other:
                return True
        return False

    def __repr__(self):
        return ",".join(map(str,self.values))

for line in content:
    if "=!" in line.split(" "):
        varname = line.split(" ")[0]
        varname = sup()
        for ele in (line.split(" ")[2]).split(","):
            varname.setvalue(ele)
        for line in content:
            if varname

for line in content:
    line = line.strip("\n")
    print(line)
