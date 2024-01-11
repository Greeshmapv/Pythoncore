from abc import ABC
class Shape(ABC):
    def area(self):
        print("area of the shape")
    def perimeter(self):
        print("perimeter of the shape")
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        print("area of circle=",3.14*self.radius*self.radius)
    def perimeter(self):
        print("perimeter of circle=",2*3.14*self.radius)
class Square(Shape):
    def __init__(self,side_length):
        self.side_length=side_length
    def area(self):
        print("area of square=",self.side_length*self.side_length)
    def perimeter(self):
        print("perimeter of square=",4*self.side_length)
c=Circle(5)
c2=Square(3)
c.area()
c.perimeter()
c2.area()
c2.perimeter()