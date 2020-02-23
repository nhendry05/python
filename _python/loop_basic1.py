#Biggie Size
def big(biggie):
    for i in range (0, len(biggie), 1):
        if biggie[i]>0:
            biggie[i] = "big"
    return biggie
biggie = [-1, 3, 5, -5]
big(biggie)

#Count Positives
def positives(count):
    sum = 0
    for i in range (0, len(count), 1):
        if count[i]>0:
            sum = sum + 1
    count[len(count)-1] = sum
    return count
count = [-1,1,1,1]
positives(count)

#Sum Total
def total(myList):
    sum = 0
    for i in range(0, len(myList), 1):
        sum = sum + myList[i]
    return sum
myList = [1, 2, 3, 4]
total(myList)

#Average
def average(myList):
    if myList == []:
        return False
    else:
        sum = 0
        for i in range(0, len(myList), 1):
            sum = sum + myList[i]
    return sum/len(myList)
average(myList)

#Length
def length(myList):
    return len(myList)
length(myList)

#Minimum
def minimum(myList):
    if myList == []:
        return False
    else:
        min = myList[0]
        for i in range(0, len(myList), 1):
            if myList[i] < min:
                min = myList[i]
    return min
minimum(myList)

#Maximum
def maximum(myList):
    if myList == []:
        return False
    else:
        max = myList[0]
        for i in range(0, len(myList), 1):
            if myList[i] > max:
                max = myList[i]
    return max
maximum(myList)

#Ultimate Analysis
def analysis(myList):
    ultimate = {}
    ultimate["sumTotal"] = total(myList)
    ultimate["average"] = average(myList)
    ultimate["minimum"] = minimum(myList)
    ultimate["maximum"] = maximum(myList)
    ultimate["length"] = length(myList)
    return ultimate
analysis(myList)

#Reverse List
def reverse(revList):
    y = len(revList) -1
    x = int(y/2)
    for i in range (0, x, 1):
        temp = revList[i]
        revList[i] = revList[y-i]
        revList[y-i] = temp
    return revList
reverse([1,2,3,4,5])