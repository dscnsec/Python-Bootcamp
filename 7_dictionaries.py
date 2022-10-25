#This is a python script to demonstrate dictionaries

#This is a dictionary
#Dictionaries are used to store data values in key:value pairs
myDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

#add an item to the dictionary
myDict["color"] = "red"

#remove an item from the dictionary
myDict.pop("model")

#remove the last item from the dictionary
myDict.popitem()

#remove all items from the dictionary
myDict.clear()

#copy the dictionary
myDict2 = myDict.copy()

#join two dictionaries
myDict3 = dict(myDict, **myDict2)

#Dictionary methods
#get() - returns the value of the specified key
#items() - returns a list containing a tuple for each key value pair
#keys() - returns a list containing the dictionary's keys
#pop() - removes the element with the specified key
#popitem() - removes the last inserted key-value pair
#values() - returns a list of all the values in the dictionary
