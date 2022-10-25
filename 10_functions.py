#This is a python script to demonstrate functions

#This is a function
#Functions are used to perform a specific task
def myFunction():
    print("Hello World")

#This is a function with parameters
#Parameters are used to pass data to a function
def myFunction2(name):
    print("Hello " + name)

#This is a function with default parameters
#Default parameters are used to set a default value for a parameter
def myFunction3(name = "GDSC"):
    print("Hello " + name)

#This is a function with return values
#Return values are used to return data from a function
def myFunction4(name):
    return "Hello " + name

#This is a function with variable number of arguments
#Variable number of arguments are used to pass a variable number of arguments to a function
def myFunction5(*names):
    for name in names:
        print("Hello " + name)

#This is a function with variable number of keyword arguments
#Variable number of keyword arguments are used to pass a variable number of keyword arguments to a function
def myFunction6(**names):
    for name in names:
        print("Hello " + names[name])

#This is a function with a lambda expression
#Lambda expressions are used to create anonymous functions
myFunction7 = lambda name : "Hello " + name

#This is a function with a docstring
#Docstrings are used to describe a function
def myFunction8(name):
    """This function prints Hello and the name passed as a parameter"""
    print("Hello " + name)

#This is a function with a recursive call
#Recursive calls are used to call a function from within itself
def myFunction9(x):
    if x > 0:
        print(x)
        myFunction9(x - 1)

