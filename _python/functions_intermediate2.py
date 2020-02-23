#Nicole Hendry
#Intermediate Functions 2

#1 Update Values in  Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
x[1][0] = 15 #changes value 10 in x to 15
students[0]['last_name'] = 'Bryant' #changes last_name of first student from 'Jordan' to 'Bryant'
sports_directory['soccer'][0]= 'Andres' #changes 'Messi' to 'Andres' in sports_directory
z[0]['y'] = 30 #changes value 20 in z to 30

#2 Interate through a List of Dictionaries
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(students):
    for i in range(0, len(students), 1):
        print("\n")
        for key in students[i]:
            x = [key]
            y = students[i][key]
            print("{} - {}," .format(*(x), y), end = " ")
#iterateDictionary(students)

#Get Values From a List of Dictionaries
def iterateDictionary2(key_name= '', some_list= ''):
    for i in range(0, len(students), 1):
        if key_name == "first_name":
            print(students[i]['first_name'])
        elif key_name == "last_name":
            print(students[i]['last_name'])
#iterateDictionary2(key_name = "last_name", some_list = "students")

#Iterate Through a Dictionary with List Values
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(dojo):
    for k in dojo:
        y = dojo[k]
        print("\n")
        print(len(dojo[k]), end ="")
        print(" {}".format(k))
        for y in dojo[k]:
            print(y)
printInfo(dojo)