class Vehicle:
    def __init__(self,make,model):
        self.make=make
        self.model=model
    def start(self):
        print("welcome to my showroom",self.make)
    def stop(self):
        print("thanks for comming",self.make)
class Car(Vehicle):
    def function(self,num_doors):
        self.num_doors=num_doors
        print("brand of car:",self.make,"\n","model is:",self.model)
        print("number of doors on car",self.num_doors)
class Motorcycle(Vehicle):
    def function(self,two_wheels):
        self.two_wheels=two_wheels
        print("brand of motorcycle:",self.make,"\n","model is:",self.model)
        print("the number of doors on",self.two_wheels)
c1=Car("lamborgini","urus")
c1.start()
c1.function(4)
c1.stop()
c2=Motorcycle("triumph","bobber")
c2.start()
c2.function(0)
c2.stop()
