#single inheritance

class Dog:
    def __init__(self):
        self.eat = "biscuts"
    def m1(self):
        self.voice= "bow"

class Puppy(Dog):
    def m2(self):
        print(self.eat,self.voice)
        print("dog and puppy eats buscuits and bark bow")

child = Puppy()
child.m1()
child.m2()


#multiple level inheritance
       # inheritance properties from multiple level classes to single single


class Swim:
    def __init__(self):
        self.swim = "water"
        print("duck swim in water")

class Fly(Swim):
    def m1(self):
        self.flyswim = "sky"
        print("duck fly in the sky")

class Duck(Fly):
    def m2(self):
        self.duckvoice ="quack"
        print(self.swim)
        print(self.flyswim)
        print(self.duckvoice)

s = Duck()
s.m1()
s.m2()      


#multiple inheritance
   # inheriting properties from multiple class to single class

class Engine:
    def m1(self):
        self.engine = "engine starting"
class Wheels:
    def m2(self):
        self.wheels = "wheels rolling"
class car(Engine,Wheels):
    def m3(self):
        print(self.engine +  self.wheels)

child =car()
child.m1()
child.m2()
child.m3()


#hirachical
   #inherits properties from single class to multiple class

class P:
    def _init_(self):
        self.name = "mahesh"
class C1(P):
    def m1(self):
        print("Hello", self.name ,"this is mythri movie makers naveen")
class C2(P):
    def m2(self):
        print("Hi", self.name ,"this is director puri jagan")

c1 = C1()
c1.m1()
c2 = C2()
c2.m2()                        