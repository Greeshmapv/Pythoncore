class Employee:#class creation
    def __init__(self,name,code,salary):
        self.name=name
        self.code=code
        self.salary=salary
    def display(self):
        print("employee name:",self.name,"\n","employee code:",self.code,"\n","employee salary:",self.salary)
n=input("enter the name:")
c=int(input("enter the code:"))
s=int(input("enter the salary:"))
p1=Employee(n,c,s)
p1.display()