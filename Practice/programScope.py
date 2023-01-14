
# Examples of program scope

# Global variable defined outside function
name = "Python"


def getName():
    # Local (just for this function) defined inside function
    name = "C#"
    print("I am coding with {}".format(name))

getName()

# Will print global variable value not the local from inside function
print(name)
