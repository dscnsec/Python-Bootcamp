#This is a python script to demonstrate tuples

#This is a tuple
#Tuples are used to store multiple items in a single variable
myTuple = ("apple", "banana", "cherry")
print(myTuple)

#join two tuples
myTuple2 = myTuple + ("orange", "mango")
print(myTuple2)

#tuple slicing
myTuple3 = myTuple2[1:4]
print(myTuple3)

#Difference between lists and tuples
#Lists are mutable, tuples are immutable
#Lists can be modified, tuples cannot be modified
#Lists use [], tuples use ()

#Use tuples when you do not want to modify the data
#Use lists when you want to modify the data

#Tuple methods
#count() - returns the number of times a specified value occurs in a tuple
#index() - searches the tuple for a specified value and returns the position of where it was found

