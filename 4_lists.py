#This is a python script to demonstrate lists

#This is a list
#Lists are used to store multiple items in a single variable
myList = ["apple", "banana", "cherry"]

#add an item to the end of the list
myList.append("orange")

#add an item at a specific index
myList.insert(1, "mango")

#remove an item from the list
myList.remove("banana")

#remove an item at a specific index
myList.pop(1)

#remove the last item from the list
myList.pop()

#remove all items from the list
myList.clear()

#reverse the order of the list
myList.reverse()

#sort the list
myList.sort()

#copy the list
myList2 = myList.copy()

#join two lists
myList3 = myList + myList2

#list slicing
myList4 = myList[1:3]

#List methods
#append() - adds an element at the end of the list
#clear() - removes all the elements from the list
#copy() - returns a copy of the list
#count() - returns the number of elements with the specified value
#extend() - add the elements of a list (or any iterable), to the end of the current list
#index() - returns the index of the first element with the specified value
#insert() - adds an element at the specified position
#pop() - removes the element at the specified position
#remove() - removes the item with the specified value
#reverse() - reverses the order of the list
#sort() - sorts the list

