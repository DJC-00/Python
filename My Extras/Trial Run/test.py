
from cgi import test

tes = [1,1,1,1,1]
testArr = [12,53,75,25,16,201,77,32,123,63];
nTestArr = [-12,53,-75,25,-16,201,-77,32,-123,63];

def print_1_255():
    for i in range (1,256,1):
        print(i);

def printOdds():
    for i in range(1,256,2):
        print(i);

def sum255():
    sum = 0;
    for i in range (1,256):
        sum += i;
    return (sum);

def printArray(arr):
    for i in range (len(arr)):
        print(arr[i]);

def printMax(arr):
    max = 0;
    for i in range (len(arr)):
        if arr[i] > max:
            max = arr[i];
    return (max);

def printAvg(arr):
    fSum = 0
    avg = 0;
    for i in range(len(arr)):
        fSum += arr[i];
    avg = fSum/len(arr);
    return (str(fSum) + " / " + str(len(arr)) + " = " + str(avg));

def oddArray():
    odds = [];
    for i in range(1,256,2):
        odds.append(i);
    return odds;

def squaredArr(arr):
    newArr = arr.copy();
    print(newArr)
    for i in range(len(arr)):
        newArr[i] = pow(newArr[i],2);
    return newArr;

def greaterThan(arr, x = int):
    gNum = 0;
    higherNums = [];
    for i in range(len(arr)):
        if testArr[i] > x:
            gNum += 1;
            higherNums.append(arr[i]);
    return gNum, higherNums;

def noNegatives(arr):
    cpyArr = arr.copy();
    for i in range(len(cpyArr)):
        if cpyArr[i] < 0:
            cpyArr[i] = 0;
    return cpyArr;

def minMaxAvg(arr):
    funArr = []
    max = arr[0];
    min = arr[0];
    avg = 0;
    
    for i in range (len(arr)):
        avg += arr[i]
        if arr[i] > max:
            max = arr[i];
        elif arr[i] < min:
            max = arr[i];

    funArr.append("Min= ")
    funArr.append(min)
    funArr.append("Max= ")
    funArr.append(max)
    funArr.append("Avg= ")
    funArr.append(avg/len(arr))
    return (funArr);

print_1_255();
print ("------------------------------------")
printOdds();
print ("------------------------------------")
print(sum255());
print ("------------------------------------")
printArray(testArr);
print ("------------------------------------")
print(printMax(testArr));
print ("------------------------------------")
print(printAvg(testArr));
print ("------------------------------------")
print(oddArray());
print ("------------------------------------")
print(squaredArr(testArr));
print ("------------------------------------")
print(greaterThan(testArr,33));
print ("------------------------------------")
print(noNegatives(nTestArr));
print ("------------------------------------")
print(minMaxAvg(testArr));