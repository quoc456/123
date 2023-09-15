import math
class Complex:
    def __init__(self,*args):
        if len(args)==0:
            self.a=1
            self.b=2
        elif len(args)==2:
            self.a=args[0]
            self.b=args[1]
    def Read(self):
        A=input()
        self.a=A.split(" ")[0]
        self.b=A.split(" ")[1]
    def __str__(self):
        if self.b>=0: 
            return ("%d+%d*i"%(self.a,self.b))
        else: return ("%d%d*i"%(self.a,self.b))
    def print(self):
        if self.b>=0:
            print ("%d+%d*i"%(self.a,self.b))
        else: print ("%d%d*i"%(self.a,self.b))
    def getModule(self):
        return math.sqrt(float(math.pow(self.a,2))+float(math.pow(self.b,2)))
    def __sub__(self,other):
        self.a=self.a+other.a
        self.b=self.b+other.b
        return self
a=Complex(1,2)
b=Complex(-5,-8)
# print(a.__sub__(b))
print(a-b)
print(a.getModule())