##Here's some code i wrote
print((lambda a,b: a*b)((lambda:int(input()))(),(lambda:int(input()))()))
print((lambda: (1 + ((lambda a:a)(5))))())


#Oh and also

class wtf(object):
    def wtf2(self):
        def wtf3(self):
            return (lambda: "wtf4")()
