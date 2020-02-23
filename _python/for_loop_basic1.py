#Nicole Hendry
#Loops: Basic I

#Basic
for basic in range(0, 151, 1):
    print(basic)

#Multiples of five
for multiples in range (5, 1001, 5):
    print(multiples)

#Counting, the Dojo Way
for dojo in range (1, 101, 1):
    if dojo%10 == 0:
        print("Coding Dojo")
    elif dojo%5 == 0:
        print("Coding")
    else:
        print(dojo)

#Whoa, That sucker's huge
sum = 0
for huge in range (0, 500001, 1):
    if huge%2 != 0:
        sum = sum + huge
print(sum)

#Countdown by Fours
for fours in range (2018, 0, -4):
    print(fours)

#Flexible Counter
lowNum = 2
highNum = 9
mult = 3
for flex in range (lowNum, highNum+1, 1):
    if flex%mult == 0:
        print(flex)