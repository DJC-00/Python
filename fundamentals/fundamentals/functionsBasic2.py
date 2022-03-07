def countDown(num):
    countDownList = ""
    for i in range(num, 0, -1):
        countDownList += str(i) + " "
    return countDownList

def printAndReturn(a,b):
    print(a)
    return b

def firstPlusLen(arr):
    return arr[0]+len(arr);

def greaterThan(arr):
    newArr = []
    for i in range(len(arr)):
        if (arr[i] > arr[1]):
            newArr.append(arr[i])
    return newArr;

def mkArr(length, value):
    newArr = []
    for i in range(length):
        newArr.append(value)
    return newArr

print(countDown(20))

print(printAndReturn(2,3))

print(firstPlusLen([1,3,5]))

print(greaterThan([1,4,5,1,2,66,3,55,2]))

print(mkArr(2,3))