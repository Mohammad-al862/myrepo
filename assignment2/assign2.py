#1.write a program which can filter even numbers in a list by using filter function.the list is [1,2,3,4,5,,6,7,8,9,10]

l = [1,2,3,4,5,6,7,8,9,10]
l1 = filter(lambda x:x if x%2 ==0 else False,l)
print(list(l1))

#2. write a write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10]

l =[1,2,3,4,5,6,7,8,9,10]
def sqr(a):
       return a*2
l1 = map(sqr,l)
print(list(l1))


#3. write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10]

l = [1,2,3,4,5,6,7,8,9,10]
def sqr(a)  iseven(x):
        if x ==0:
          return a*2
        l1= map(sqr,l)
l2= filter(lambda x:x if x%2 ==0 else False,l1)
print(list(l1))
print(list(l2))


       


 



#4. write a program which can filter() to make a list whose elements are even number between 1 and 20

l1 = filter(lambda x:x if x%2 ==0 else False,range(1,20))
print(list(l1))

#5. write a program which can map() to make a list whose elements are square of numbers between 1 and 20


if l in range(1,20):
 def sqr(a):
    return a*2
l1 = map(sqr,l)
print(list(l1))


