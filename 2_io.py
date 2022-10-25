#This is a python script to demonstrate input and output

#use the input() function to get input from the user
#the input() function returns a string
#the input() function takes a string as an argument
#the string is displayed as a prompt to the user
#the input() function can be used to get input from the user

#input a string
myString = input("Enter a string: ")
print(myString)

#input an integer
myInt = int(input("Enter an integer: "))
print(myInt)

#input a float
myFloat = float(input("Enter a float: "))
print(myFloat)

#type conversion
#int() - converts to integer
#float() - converts to float
#str() - converts to string

#map function
#map() - applies a function to every item in an iterable

#input a list of integers
myList = list(map(int, input("Enter a list of integers: ").split()))
print(myList)