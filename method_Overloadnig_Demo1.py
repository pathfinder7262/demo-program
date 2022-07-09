class a:
    def m1(self):
        print("M1 1st method")

    def m1(self, x):
        print("M1 2nd method")

    def m1(self,  c , b):
        print("M1 3rd method")

A = a()
A.m1()
