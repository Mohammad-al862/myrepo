#write a python program to merge a two list?

l1 = ["house","farm"]
l2 = ["hut","cave"]

l1.extend(l2)
print(l1)

#write a python program to delete element of given index in list?

n = [10,20,21,22.3,30]
print(n.pop(3))
print(n)

#write a program to delete given element from the list?

nums = [1,2,3,4,5,6,7]
n1 = ["orange","apple","grape"]
nums.remove(4)
n1.remove("orange")
print(nums)
print(n1)

#write a python program to check if the two list are having atleast one common element?

l1 = [1,2,3,4]
l2 = [7,8,9,1]
set1 = set(l1)
set2 = set(l2)
if set1.intersection(set2):
    print("the two lists have atleast one common element.")
else:
    print("the two lists do not have any common elements.") 



#write a python program to remove specified column from the  nestdiest?

l3 =[[1,2,3],[4,5,6],[7,8,9]]
column_index = 1
for sublist in l3:
    del sublist[column_index]
print("nested list after removing column")



#write a python program to convert a list of integers into single integers?
     
lst = [2,4,5,6]
for i in lst:
    print(i, end="")