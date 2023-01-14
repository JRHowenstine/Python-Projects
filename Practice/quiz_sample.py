def getName(name =""):
    name = askName(name)
    print("I loe \n blah {}.".format(name))

def askName(name):
    go=True
    while go:
        if name == "":
            name = input("name please:\n>>>")
        if name != "":
            go=False
        return name

if __name__ == '__main__':
    getName()
