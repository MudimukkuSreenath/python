class Example:
    c,d=20,30

    def __init__(self):
        self.a=10
        self.b=20
    @staticmethod
    def m1():
        print(c+d)
        
class Ex(Example):
    def m2(self):
        print(self.a-self.b)
obj=Ex()
obj.m2()
Example.m1()
#base.m1()
