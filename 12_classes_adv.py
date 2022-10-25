#This is a python script to demonstrate advanced features of classes

#This is a class
#Classes are used to create objects

class MyClass:
    
    classVariable = "Hello World"
    #This is a constructor
    #Constructors are used to initialize the object
    def __init__(self, name):
        #This is an instance variable
        #Instance variables are variables that are unique to each object of the class
        self.name = name

        #public variables are accessible from outside the class
        self.publicVariable = "Hello Parent"
        #protected variables are accessible from within the class and its subclasses
        self._protectedVariable = "Hello Parent"
        #private variables are accessible only from within the class
        self.__privateVariable = "Hello Parent"


    #This is a method
    #Methods are functions that are defined inside a class
    def myMethod(self):
        print("Hello " + self.name)


#Inheritance is used to define a class that inherits all the methods and properties from another class
#The child class will inherit all the methods and properties from its parent class
#The child class can add its own methods and properties in addition to the parent class methods and properties
class MyChildClass(MyClass):
    
    #This is a constructor
    #Constructors are used to initialize the object
    def __init__(self, name):
        #This is a call to the parent class constructor
        #The super() function returns a reference to the parent class
        super().__init__(name)

        #This is an instance variable
        #Instance variables are variables that are unique to each object of the class
        self.childName = name

        #public variables are accessible from outside the class
        self.childPublicVariable = "Hello Child"
        #protected variables are accessible from within the class and its subclasses
        self._childProtectedVariable = "Hello Child"
        #private variables are accessible only from within the class
        self.__childPrivateVariable = "Hello Child"

    def myChildMethod(self):
        print("Hello " + self.childName)

    #method overriding is used to override a method in the parent class
    def myMethod(self):
        print("Hello " + self.childName)
    

#This is an object
#Objects are instances of a class
myObject = MyClass("Alpha")

#This is a call to the object method
myObject.myMethod()

#This is an object
#Objects are instances of a class
myChildObject = MyChildClass("Beta")

#This is a call to the object method
myChildObject.myChildMethod()

#This is a call to the object method
myChildObject.myMethod()

#Calling the parent class method using the super() function
super(MyChildClass, myChildObject).myMethod()

