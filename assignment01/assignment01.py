#1 write a program which will find all such numbers which are divide by 7 but are not a multiple of 5, between 2000 and 3200. the numbers obtained should be printed in a comma-separated on a single line.


d =[]
for i in range(2000,3200):
    if i%7 ==0 and i%5!=0:
      d.append(i)
      print(d)


#2 write a given integral number n, write a program to generate a dictionary that contains(i,i*i) such that is an integer number between 1 and n. and then the program should print the dictionary. suppose the followig input is supplied to the program:8 then,the output should be:{1:1,2:4,3:9,4:16,5:25,6:36,7:49,8:64}

n=8
d = {}
for i in range(1,n+1):
 d[i]=i*i
print(d)   

#9 define a function which can print a dictionary where the keys are numbers between 1 and 20 and the values are square of keys
 

d ={}
for num in range(1,20):
 d[num] = num*2
print(d)


#10 define a function which can generate list where the value are square of numbers between 1 and 20 then the function needs to be print the last five elements in the list 


d =[]
for i in range(1,21):
  d.append(i*i) 
print(d[-5:])

#3.write a program which aceepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.suppose the following input is supplied to the program: 34,67,55,33,12,98 then,the output shuld be:
 
input_numbers =input("enter a sequence of comma-separated numbers:")
numbers_list = [int(num) for num in input_numbers.split(',')]
numbers_tuple =tuple(numbers_list)
print(numbers_list)
print(numbers_tuple)

#8.

input_username =input("enter the username:")
input_password = input("enter the password:")
