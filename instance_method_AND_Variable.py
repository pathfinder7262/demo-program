#instance_method_AND_Variable
class inst():
    def __init__(self,nm,rn):
        self.name = nm
        self.rollno = rn
        print('name1 :',self.name )
    
    def show(self,ag):
        print("name: ",self.name)
        print("Roll No: ",self.rollno)
        self.age = ag
        print("age: ",self.age)

i = inst('chetan',10)
i.gender = 'male'
i.show(23)
print("Gender : ",i.gender)
print(i.__dict__)
del i.name
print(i.__dict__)

