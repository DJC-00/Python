for i in range(151):
    print(i)

for i in range(0,1001,5):
    print(i)

for i in range(101):
    if (i%10) == 0:
        print("Coding Dojo")
    elif (i%5) == 0:
        print("Coding")
    else:
        print(i)

mySum = 0
for i in range(1,500000,2):
    mySum += i;
    
print(mySum)

for i in range(2018,0,-4):
    print(i)

print("------------------------------------------------")

lowNum = 2
highNum = 9
mult = 3

for i in range(lowNum,highNum+1):
    if(i%int(mult) == 0):
        print(i)