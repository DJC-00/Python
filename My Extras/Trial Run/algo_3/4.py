
testArray=[[1,2,3],[11,22,12,23,34],[0,9]];

def findVal2D(x = int):                     # function findVal2D(value)
    for i in range(len(testArray)):             # for (var i = 0; i < testArray.length; i++)
        for j in range(len(testArray[i])):          # for (var j = 0; j < testArray[i].length; j++)
            if testArray[i][j] == x:
                print("Value " + str(x) + " was found at arr[" + str(i) + "][" + str(j) + "]")
                return
    print("Value not found")

findVal2D(11)
findVal2D(99)


#   function findVal2D(value){
#       for (var i = 0; i < testArray.length; i++){
#           for (var j = 0; j < testArray[i].length; j++){
#               if (testArray[i][j] == x){
#                   console.log("Value " + x + " was found at arr[" + i + "][" + j + "]")
#                   return
#               }
#           }
#       }
#       console.log("Value not found")
#   }
