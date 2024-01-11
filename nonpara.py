class Person:
    def __init__(self):
        print("welcome")
    def display(self,name,age):
        self.name=name
        self.age=age
        print("my name is :",self.name," my age is",self.age)
p1=Person()
p1.display("greeshma",23)