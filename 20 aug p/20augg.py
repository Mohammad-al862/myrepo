# polymorphism 

# method overloading
#operator overloading

print("ram"+"krishna")
print(1+2)

class Marks:
    def __init__(self,marks):
        self.marks = marks

    def _add_(self,abc):
        return self.marks + abc.marks

    def _mul_(self,num):
        return self.marks * num.marks

p1 = Marks(25)
p2 = Marks(45)
print(p1+p2) 

p3 = Marks(10)
print(p1*p3)


#method overloading

def sum(a,b):
    print(a+b)
def sum(x,y):
    print(x*y)

sum(20,30)

#constructer overloading

class Score:
    def __init__(self,score):
        self.score = score
        print(score, "constructer-1")

    def _init_(self,score):
        self.score = score
        print(score, "constructer-2")

s = Score(20)    

#method overridding

class Showroom:
    def swift(self):
        print("spare parts, services")

    def store(self):
        print("available")

class New(Showroom):
    def store(self):
        print("not available")

c =New()
c.store()                    


#


class Tata:
    def __init__(self,tea,motor):
        self.tea =tea
        self.motor = motor
        print(tea,motor)

class Tata:
    def __init__(self,tea,motor,zudio):
        self.tea =tea
        self.motor = motor
        self.zudio = zudio
        print(tea,motor,zudio)

t = Tata("powder","nexon","t-shirt")            


