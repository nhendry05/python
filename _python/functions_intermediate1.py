#Nicole Hendry
#Intermediate Function 1

import random


def randInt(min= 0, max= 100):
    if max<0 and min == 0:
        print("Error: set minimum value to be less than maximum value, default value is 0")
    elif min>max:
        print("Error: set maximum value to be higher than minimum value, default value is 100")
    else:
        num = (random.random()) * (max-min) + min
        print(round(num))

# should print a random integer between 0 to 100
print(randInt())
# should print a random integer between 0 to 50
print(randInt(max=50))
# should print a random integer between 50 to 100
print(randInt(min=50))
# should print a random integer between 50 and 500
print(randInt(min=50, max=500))
# error message if maximum value is less than 0 and minimum at default
print(randInt(max=-500))
# error message if minimum value is higher than maximum value
print(randInt(min=500))
