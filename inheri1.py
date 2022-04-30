class vehicle():
    comp = "Tata"
    def __init__(self,wheel,clr,mdl,yop):
        self.model = mdl
        self.color = clr
        self.wheel = wheel
        self.yop = yop
        self.capacity = 50

    def show(self):
        print("Model Name: ",self.model )
        print("Color: ",self.color)
        print("Wheels: ",self.wheel)
        print("Year of Passing: ",self.yop)
        print("capacity: ",self.capacity)
        print("Company is: ",vehicle.comp)

class car(vehicle):
    def __init__(self, wheel, clr, mdl, yop,eng):
        super().__init__(wheel, clr, mdl, yop)
        self.engine = eng

    def show(self):
        super().show()
        print("Engine: =",self.engine)

class truck(car):
    pass


c1 = car(4,'black',"nano",2016,'22hp')
c1.show()
print("++++++++")
t1 = truck(12,'yello','hammer',2022,'400hp')
t1.show()