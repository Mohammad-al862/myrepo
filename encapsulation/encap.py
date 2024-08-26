# encapsulation > it is the process of biding all class attributes into single entity or class is called encapsulation.

# using private members: members are accesible only with in the class.
# using public  members : members are aceesible from outside of class.
#using protected members:members are aceesible from class and subclass. 

#public members. 

class Demo():
    def __init__(self,a,b):
        self.__a = a        #private
        self._b = b         #protected
class Demo2(Demo):
    def output(self):
        print(self._b)  

d =Demo2(3,4)
d.output()

# accessing private and protected members

class Demo():
        __a=2 #private
        _b=3   #protected
        print(__a)
        print(_b)
        

