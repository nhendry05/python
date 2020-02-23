#Nicole Hendry
#Functions Basic II

#Countdown
def countdown(x):
    listOne = []
    for x in range (x, -1, -1):
        listOne.append(x)
    return listOne
x = 5

#Print and Return
def printReturn (listTwo):
    print(listTwo[0])
    return(listTwo[1])
printReturn([2,3])

#First Plus Length
def firstLength (listThree):
    a = listThree[0]
    b = len(listThree)
    return a+b
listThree = [1,2,3,4,5]
firstLength(listThree)

#Values Greater than Second
def greaterSecond(listFour):
    newList = []
    if len(listFour)<2:
        return False
    for i in range (0, len(listFour), 1):
        if listFour[i] > listFour[1]:
            newList.append(listFour[i])
    return newList
listFour = [5, 2, 3, 2, 1, 4]
greaterSecond(listFour)
#This Length, That Value
def lengthValue(size, value):
    listFive = []
    for i in range (0, size, 1):
        listFive.append(value)
    return listFive
lengthValue(6, 2)
