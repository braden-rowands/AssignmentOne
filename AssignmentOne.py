userName = input("Please enter your name")

def menuChoice():
    useChoice = input("Please enter a choice between list of completed items, list of required items or to quit")
    while "CRQ" not in useChoice:
        useChoice = input("Please enter a choice between list of completed items, list of required items or to quit")

def loadFile():
    itemsList = []
    listFile = open('items', 'w')
    for data in listFile:
        itemsList.append(data)