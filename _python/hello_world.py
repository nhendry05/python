# 1. TASK: print "Hello World"
print("Hello World")
# 2. print "Hello Noelle!" with the name in a variable
name = "Nicole"
print("Hello", name,"!")	# with a comma
print("Hello " + name + "!")	# with a +
# 3. print "Hello 42!" with the number in a variable
number = 5
print("Hello", number, "!")	# with a comma
#print("Hello" + number "!")	# with a +	-- this one should give us an error!
newNumb = "5"
print("Hello " + newNumb + "!")
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "mac and cheese"
print("I love to eat {} and {}." .format(fave_food1, fave_food2 )) # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}.") # with an f string

# others ways
# %formatting
first = "My name is %s!" %"Nicole"
print(first)
#built in
built = "This IS an ExAmPlE"
print(built.upper())
print(built.lower())
print(built.split())

sub = "an"
print(built.count(sub))
print(built.find(sub))