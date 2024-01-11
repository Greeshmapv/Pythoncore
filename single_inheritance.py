class Animal:
   def __init__(self,name):
        self.name=name
   def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        print("says woof...",self.name)
class Cat(Animal):
    def speak(self):
        print("says meow...",self.name)
d=Dog("puppy")
d.speak()
c=Cat("aavu")
c.speak()
