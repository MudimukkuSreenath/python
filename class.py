class First:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        print("iam constructor")
    def sum(self):
        res=self.a+self.b
        print(res)
    '''def __str__(self):
        print("a="+str(self.a)+"b="+str(self.b))'''
    def __del__(self):
        print("iam destructor")
obj=First(10,20)
print(obj)
obj.sum()