#This is a python script to demonstrate classes

#This is a class
#Classes are used to create objects

class MyClass:
    #This is a docstring
    #Docstrings are used to describe a class
    """This class prints Hello and the name passed as a parameter"""

    #This is a class variable
    #Class variables are variables that are shared by all objects of the class
    classVariable = "Hello World"

    #This is a constructor
    #Constructors are used to initialize the object
    def __init__(self, name):
        #This is an instance variable
        #Instance variables are variables that are unique to each object of the class
        self.name = name

        #public variables are accessible from outside the class
        self.publicVariable = "Hello World"
        #protected variables are accessible from within the class and its subclasses
        self._protectedVariable = "Hello World"
        #private variables are accessible only from within the class
        self.__privateVariable = "Hello World"


    #This is a method
    #Methods are functions that are defined inside a class
    def myMethod(self):
        print("Hello " + self.name)

    #This is a static method
    #Static methods are methods that are bound to a class and not the object of the class
    @staticmethod
    def myStaticMethod():
        print("Hello World")
    
    #This is a class method
    #Class methods are methods that are bound to the class and not the object of the class
    @classmethod
    def myClassMethod(cls):
        print("Hello World")
    
    #This is a property
    #Properties are used to define getter, setter and deleter methods
    @property
    def myProperty(self):
        #This is a getter method
        return self.__privateVariable

    @myProperty.setter
    def myProperty(self, value):
        #This is a setter method
        self.__privateVariable = value

    @myProperty.deleter
    def myProperty(self):
        #This is a deleter method
        del self.__privateVariable
    
    #This is a magic method
    #Magic methods are used to define the behavior of operators
    def __add__(self, other):
        return self.name + other.name
    

#This is an object
#Objects are instances of a class
obj = MyClass("GDSC")

#This is an object method call
#Object method calls are used to call a method of an object
obj.myMethod()

#This is an object variable access
#Object variable accesses are used to access a variable of an object
print(obj.name)