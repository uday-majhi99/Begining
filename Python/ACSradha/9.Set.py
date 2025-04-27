"""
Set is the collection of the unordered items.
Each element in the set must be unique and immutable.
syntax : Variable = {1,2,3,4,5,6}
if there is an repeated element it removes the duplicate one
null_set = set() This sets an empty set
"""
from itertools import count

set_collection = {1,2,3,"Uday","Majhi"}
print(set_collection)
print(type(set_collection))
print(len(set_collection))

set_det = set()#create a empty set
print(type(set_det))

#set methods
set_det.add(1) #add values to the set
set_det.add("Uday")
print(set_det)
set_det.remove("Uday") #removes values from set
set_det.add (("Uday","Majhi"))
print(set_det)
set_det.pop()
print("Pop",set_det)
set_det.clear()
print("Clear",set_det)

#Set methods Union and Intersection
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
print(set1.union(set2))
print(set1.intersection(set2))

#Store words and print using python dictionary
this_dicts ={
    "table": ["A piece of furniture","List of fact and figures"],
    "cat" : "A small animal"
}
print(this_dicts)

classes = {"Python","Java","C++","Python","Javascript","Java","Python","Java","C++","C"}
print(classes)
print(len(classes))