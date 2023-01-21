"""
An example of inheritence
and polymorphism
"""

# Define Parent Class
class User:
    # Define the attributes of parent class
    userName = "No User Name Provided"
    name = "No Name Provided"
    email = " "
    password = "Password"
    # Define method for parent class
    def getInfo(self):
        entry_userName = input("Please type your User name: ")
        entry_name = input("Please enter your name: ")
        entry_email = input("Please type your email address: ")
        entry_password =input("Please enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("welcome back, {}.".format(entry_name))
        else:
            print("The password or email is incorrect!")

# Define child class one 
class Customer(User):
    # Define unique attributes for child class
    address = "No Address Provided"
    customerID = "000000"

    def getInfo(self):
        entry_userName = input("Please type your User name: ")
        entry_name = input("Please enter your name: ")
        entry_email = input("Please type your email address: ")
        entry_password = input("Please enter your password: ")
        entry_Id = input("Please enter your customer ID number: ")
        if (entry_Id == self.customerID and entry_password == self.password):
            print("welcome back, {}.".format(entry_name))
        else:
            print("The password or email is incorrect!")
        

# Define child class two
class Employee(User):
    # Define unique attributes for child class
    employeeID = "0000"
    branchID = "00"
    employeePin = "1234"

    def getInfo(self):
        entry_userName = input("Please type your User name: ")
        entry_name = input("Please enter your name: ")
        entry_email = input("Please type your email address: ")
        entry_pin =input("Please enter your pin number: ")
        if (entry_email == self.email and entry_pin == self.employeePin):
            print("welcome back, {}.".format(entry_name))
        else:
            print("The password or email is incorrect!")

# Define child class three
class Guest(User):
    # This child class has no unique attributes but does have a modified method
    def getInfo(self):
        entry_userName = "Guest"
        entry_name = input("Please enter your name: ")
        entry_email = input("Please type your email address: ")
        entry_password = "password"
        if (entry_userName == Guest and entry_password == password):
            print("welcome, {}.".format(entry_name))
        
