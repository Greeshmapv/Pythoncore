class Employee:
    def __init__(self,name,empcode,salary):
        self.name=name
        self.empcode=empcode
        self.salary=salary
    def display(self):
        print("name of the employee=",self.name,"\n","employee code:",self.empcode,"\n","salary:",self.salary)
p1=Employee("greeshma",310,280000)
p1.display()