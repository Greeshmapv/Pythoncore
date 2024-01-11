class Person:
    def __init__(self,name,age):#parameterized constructor
        self.name=name
        self.age=age
    def display(self):
        print("my name is:",self.name," my age is",self.age)
p1=Person("greeshma",23)
p1.display()
