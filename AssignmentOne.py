userName = input("Please enter your name")

def menuChoice():
    useChoice = input("Please enter a choice between list of completed items, list of required items or to quit")
    while useChoice != "Q":
        if useChoice == "R":
            print ("This will show required tasks")
        elif useChoice == "C":
            print("This will show completed tasks")
        else:
            useChoice = input("Please enter a valid choice between Q,R or C")

def loadFile():
    itemsList = []
    listFile = open('items.csv', 'r')
    for data in listFile:
    itemsList.append(data)
        #   print(data)


secondList= []
for i in itemsList:
    newText = i.split(",")
    secondList.append(newText)
print(secondList)