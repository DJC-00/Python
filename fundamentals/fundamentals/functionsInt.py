x = [ [5,2,3], [10,8,9] ] 
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def updateVal1(arr, oldVal, newVal):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if (arr[i][j] == oldVal):
                arr[i][j] = newVal;
    print(arr)

def updateVal2(objList, oldName, newName):
    for i in range(len(objList)):
        if (objList[i]['last_name'] == oldName):
            objList[i]['last_name'] = newName
    print(objList)

def updateVal3(spDir,oldName, newName):
    for items in spDir.values():
        for value in range(len(items)):
            if (items[value] == oldName):
                items[value] = newName
    print(spDir)

def dictIter(dictList):
    for i in range(len(dictList)):
        print(dictList[i])

def dictIter2(dictList, keyName):
    for i in range(len(dictList)):
        print(dictList[i][keyName])

def printInfo(dict):
    for key,value in dict.items():
        print(key + " " + str(len(value)))
        for lValue in range(len(value)):
            print(value[lValue])
        print("-----------------------------------------")



updateVal1(x, 10, 15)
print("-----------------------------------------")
updateVal2(students, "Jordan", "Bryant")
print("-----------------------------------------")
updateVal3(sports_directory,"Messi", "Andres")
print("-----------------------------------------")
dictIter(students)
print("-----------------------------------------")
dictIter2(students, 'first_name')
dictIter2(students, 'last_name')
print("-----------------------------------------")
printInfo(dojo)
