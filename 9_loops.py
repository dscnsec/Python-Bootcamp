#This is a basic python script to demonstrate loops

#This is a for loop
#For loops are used to iterate over a sequence
for i in range(5):
    print(i)

#This is a while loop
#While loops are used to iterate over a condition
i = 0
while i < 5:
    print(i)
    i += 1

#This is a nested loop
#Nested loops are loops within loops
for i in range(5):
    for j in range(5):
        print(i,j)

#This is a break statement
#Break statements are used to break out of a loop
for i in range(5):
    if i == 3:
        break
    print(i)

#This is a continue statement
#Continue statements are used to skip the current iteration of a loop
for i in range(5):
    if i == 3:
        continue
    print(i)

#This is a pass statement
#Pass statements are used to do nothing
for i in range(5):
    if i == 3:
        pass
    print(i)

#This is a loop with an else statement
#Else statements are executed when the loop is finished
for i in range(5):
    print(i)
else:
    print("Loop is finished")

#This is a loop with an else statement
#Else statements are executed when the loop is finished
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("Loop is finished")

#Iterating over a list
#Lists are mutable
list = [1,2,3,4,5]
for i in list:
    print(i)

#Iterating over a dictionary
#Dictionaries are key value pairs
dict = {"name":"GDSC","age":1}
for i in dict:
    print(i)

#Iterating over a tuple
#Tuples are immutable
tuple = (1,2,3,4,5)
for i in tuple:
    print(i)

#Iterating over a set
#Sets are unordered and unindexed
set = {1,2,3,4,5}
for i in set:
    print(i)

#Iterating over a string
#Strings are immutable
string = "Hello"
for i in string:
    print(i)