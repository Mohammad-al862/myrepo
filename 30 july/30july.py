#write a python program to a add a key to a dictionary?

d= {"name": "mahesh"}
d["age"] = "30"
d["salary"] = "35"
print(d)

#write a python program to check weather the given value is present in the dictionary or not?


d= {"name": "ajay","age": "25"}
values_to_check =  ["ajay",30]
for value in values_to_check:
 if value in d.values():
    print(f"{value} is present in the dictionary")
else:
    print(f"{value} is not present in dictionary")


#write a python program to collect data from a user and store it in dictionary,you can use python built in functions like input to get user input and then organise that output into a dictionary?


d = {}
d["name"] = input("enter the name:")
d["domaine"] = input("enter the domaine:")
d["performance"] = input("enter the performance:")
print(d)
print(type(d))

#write a python program script to  print a dictionary where the keys are numbers between 1 and 15 and the values are the square of the keys?


d = {}
for num in range(1,16):
    d[num] = num*2
    print(d)
    print(type(d))

#write a python program to ceate a dictionary from the string?

d = "{1:2,3:4,5:6,7:8}"
d = eval(d)
print(d)
print(type(d))
