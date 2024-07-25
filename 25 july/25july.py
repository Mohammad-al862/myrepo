#write a program to create a set?

s = {1,2,3,4,5,6}
print(type(s))

l = [6,7,8,9]
print(set(l))
print(type(l))


#write a program to iterate over sets?

s = {22,33,44,11,55}
for element in s:
    print(element)

#write a python program to add add memeber to a set?

s = {1,2,3,4,5,6}
s.add(8)
print(s)

#write a python program to remove item from a given set?

s = {9,8,4,2,6,7}
s.remove(9)
print(type(s))
print(s)

#write a python program to create a union of set?

carshowroom1 = {"swift","baleno","ertiga","spresoo"}
carshowroom2 = {"breeza","swift","ertiga","wagoner"}
print(carshowroom1.union(carshowroom2))
print(carshowroom1 | carshowroom2)


#write a python program to create intersection of set?

assembly = {"cheif minister","finance minister","mla","education minister"}
parlement = {"prime minister","mp","finance minister","education minister"}
print(assembly.intersection(parlement))
print(assembly & parlement)

#write a python program to create a set difference?

althaf = {"ssc","inter","btech","project"}
rakesh = {"cbsc","diploma","degree","project"}
print(althaf.difference(rakesh))
print(althaf - rakesh)

#write a program to create a symetric difference in sets?

amul = {"popsicle","butterscotch","rolled","chocolate"}
kwality = {"venela","mochi","caramel","chocolate"}
print(amul.symmetric_difference(kwality))
print(amul ^ kwality)

#write a program to find max and min values in a set?

s = {20,30,40,50,60,1,10,70}
print(max(s))
print(min(s))

#write program to update the first set with items that exists only in the first set and not in the second set?

s1 = {1,2,4,5,6}
s2 = {7,1,11,22}
s1.difference_update(s2)
print(s1)

#write a python program to remove iteams 10,20,30 from the following set at once?

s = {10,20,30,40,50,60}
s.difference_update({10,20,30})
print(s)

#check if two element are in common.if yes,display the common elements?

s = {10,20,30,40,50,60}
s.intersection_update({40,50,60})
print(s)

#update set1 by adding iteams from set2, except common items?

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print(s1.symmetric_difference(s2))

#remove items from set1 that are not common to both set1 and set2?

s1 ={1,2,3,4,5,6}
s2 = {4,5,6,7,8,9}
print(s1.difference(s2))


