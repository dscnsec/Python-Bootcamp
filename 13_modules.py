#This is a python script to demonstrate modules

#Modules are python files with a .py extension
#The module must be in the same folder or a folder specified in the sys.path
#The module name is the name of the file

#This is a import statement
#Import statements are used to import modules into the current script
import math

#This is a import statement with an alias
import math as m

#This is a import statement with a specific function
from math import sqrt

#This is a import statement with a specific function and an alias
from math import sqrt as squareRoot

#This is a import statement with all functions
from math import *


#usage of the math module
print(math.sqrt(9))

#usage of the math module with an alias
print(m.sqrt(9))

#usage of the math module with a specific function
print(sqrt(9))

#usage of the math module with a specific function and an alias
print(squareRoot(9))


