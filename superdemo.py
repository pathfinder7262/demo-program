class p:
    def __init__(self):
        print("Parent Class Constr")

    def m1(self):
        print("Parent class instance method")

    @classmethod
    def m2(cls):
        print("Parent Class m2 method class method")

    @staticmethod
    def m3():
        print("parent class static method m3")

class c(p):
    def m4(self):
        print("Child class m4 method")
        super().m1()
        self.m2()
        self.m3()
    def m1(self):
        print("Child class m1 method")
        self.__init__()
        

c = c()
c.m4()
c.m1()
