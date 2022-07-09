#abstraction 1

class Emp:
    def __init__(self,nm,acno,pin,bnm):
        self.name = nm
        self.acno = acno
        self.pin = pin
        self.bname = bnm

    def __display(self):
        print("Name: ",self.name)
        print("ACC Number: ",self.acno)
        print("Pin: ",self.pin)
        print("Bank Name: ",self.bname)

    def m1(cls):
        print("This is class method")
    

e1 = Emp("cc",123123,9900,"Axis")
#e1.display()
Emp.m1()
