

function pallindrome(testStr){
    for (var i = 0; i < testStr.length/2; i++){
        if (testStr[i] != testStr[(testStr.length-1)-i]){ //o != !
            return false
        }
    }
    return true;
}

function longestPalindrome(testStr){
    var pallArray = [];
    for (var i=0; i<testStr.length; i++){
        for (var j = testStr.length-1; j > i; j--){
            if(testStr[i] == testStr[j]){
                if (pallindrome(testStr.substr(i,j-i+1)) == true){
                    pallArray.push(testStr.substr(i,j-i+1))

                }
            }
        }
    }
    var largestIndex = 0;
    for (var i = 0; i < pallArray.length; i++){
        if (pallArray[i].length > pallArray[largestIndex].length){
            console.log(pallArray[i].length, pallArray[largestIndex].length)
            largestIndex = i;
        }
    }
    return ("'"+ pallArray[largestIndex] + "' is our longest pallindrome with a length of " + pallArray[largestIndex].length);
}

console.log(longestPalindrome("racecar dad tacocat nope aba abba"))