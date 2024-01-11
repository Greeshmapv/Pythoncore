class Student:
    def __init__(self,name,mob,address):
        self.name=name
        self.mob=mob
        self.address=address
    def display(self):
        print("name=",self.name,"\n","mobile number=",self.mob,"\n","address=",self.address)
p1=Student("greeshma",890878902,"puthiya veettil")
p1.display()