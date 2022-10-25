#This is a python script to demonstrate sets

#This is a set
#Sets are used to store multiple items in a single variable
mySet = {"apple", "banana", "cherry"}
print(mySet)

#add an item to the set
mySet.add("orange")
print(mySet)

#add multiple items to the set
mySet.update(["orange", "mango", "grapes"])
print(mySet)

#remove an item from the set
mySet.remove("banana")
print(mySet)

#remove an item from the set if it is present
mySet.discard("banana")
print(mySet)

#remove the last item from the set
mySet.pop()
print(mySet)

#remove all items from the set
mySet.clear()
print(mySet)

#copy the set
mySet2 = mySet.copy()
print(mySet2)

#join two sets
mySet3 = mySet.union(mySet2)
print(mySet3)

#Set methods
#add() - adds an element to the set
#clear() - removes all the elements from the set
#copy() - returns a copy of the set
#difference() - returns a set containing the difference between two or more sets
#difference_update() - removes the items in this set that are also included in another, specified set
#discard() - remove the specified item
#intersection() - returns a set, that is the intersection of two other sets
#intersection_update() - removes the items in this set that are not present in other, specified set(s)
#isdisjoint() - returns whether two sets have a intersection or not
#issubset() - returns whether another set contains this set or not
#issuperset() - returns whether this set contains another set or not
#pop() - removes an element from the set
#remove() - removes the specified element
#symmetric_difference() - returns a set with the symmetric differences of two sets
#symmetric_difference_update() - inserts the symmetric differences from this set and another
#union() - return a set containing the union of sets
#update() - update the set with the union of this set and others
