# Implement the concept of inheritance using python

class num:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def disp(self):
        print("The 2 Numbers: "+str(self.a)+" & "+str(self.b))

class mul(num):
    def __init__(self, a, b):
        super().__init__(a, b)
        self.prod = self.a*self.b
    def show(self):
        print("Product: "+str(self.prod))

n = mul(4,5)
n.disp()
n.show()