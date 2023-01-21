"""
Encapsulation Submission Assignment
Create a class that makes use of private and protected
attributes or functions.
"""

class Protected: #Define class and its attributes
    def __init__(self):
        self._protectedVar=10
        self.__privateVar=20
    def getPrivate(self):
        print(self.__privateVar)
    def setPrivate(self,private): #Define the functions for changing the private variable
        self.__privateVar = private

obj=Protected() #Create an object of the Protected class
print(obj._protectedVar)#Print the default value of the protected variable
obj._protectedVar=42 #Change the value of the protected variable
print(obj._protectedVar)#Print the new value of the protected variable
obj.getPrivate() #Print the default value of the private variable using function
obj.setPrivate(42) #use function to set a new value of private variable
obj.getPrivate() #Print the new value of the private variable using function
