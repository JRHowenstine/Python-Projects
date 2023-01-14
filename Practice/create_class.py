# Creating an object class in Python

# Define class name
class User:
    # Define the attributes of the class with default values
    name = "No Name Provided"
    email = ""
    password = "1234abcd"
    account = 0
    # Dunder method to attach the arguments for creating the obj to the attr of that obj
    def __init__(self, name, email, password, account):
        self.name = name
        self.email = email
        self.password = password
        self.account = account

    # Define the methods of the class
    def login(self):
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}".format(self.name))
        else:
            print("You are not authorized for this page.")
# Outside of the class you would create an instance of the User class
new_user = User("John Doe", "jdoe@outlook.com", "p@ssw0rd", 1234)
# Call the login method using the new object
new_user.login()


# Note: for simplicity of this example, we are not using any security methods to encrypt the password.
# This is not how passwords would be handled in a real-use case
