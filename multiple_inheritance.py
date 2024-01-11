class Calculation1:
    def summation(self,a,b):
        return a+b
class Calculation2:
    def multiplication(self,a,b):
        return a*b
class calculation3(Calculation1,Calculation2):
    def divide(self,a,b):
        return a/b
d=calculation3()
print(d.summation(10,20))
print(d.multiplication(10,20))
print(d.divide(10,20))