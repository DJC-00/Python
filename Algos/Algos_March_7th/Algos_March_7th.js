// Create a function that, given a string, returns the string's acronym (first letter's only, capitalized) in string form.
// Example: "there's no free lunch - gotta pay yer way" --> "TNFL-GPYW""

// Things to consider: how to move through a string? How to capitalize letters? how to create/add to a new string?

// ===================================
// with Array?
// ===================================
function acronym(str) {
    str = str.toUpperCase();
    console.log(str)
    acr = [];
    acr.push(str[0])
    for(i=0; i< str.length; i++){
        if (str[i] == " "){
            acr.push(str[i+1]);
        }
    }
    // acr = acr.toUpperCase();
    return acr;
}

console.log(acronym("there's no free lunch - gotta pay yer way"));

// ===================================
// with new String only?
// ===================================
function acronym2(str) {
    acr = "";
    acr += str[0]
    for(i=0; i< str.length; i++){
        if (str[i] == " "){
            acr += str[i+1];
        }
    }
    acr = acr.toUpperCase();
    return acr;
}

console.log(acronym2("there's no free lunch - gotta pay yer way"));

// ==================================================================================================================
// Implement reverseString(str) that takes in a String, and then returns a string of the same length, but with the characters reversed.
// Example: "creature" ---> "erutaerc"
// ** Don't use the built-in reverse() method!

// ===================================
// with Array
// ===================================
function reverseString(str) {
    revStr = [];
    for (i=str.length-1; i>=0; i--){
        revStr.push(str[i]);
    }
    return revStr;
}

console.log(reverseString("creature")); // "erutaerc"


// ===================================
// with new String only
// ===================================
function reverseString2(str) {
    revStr = "";
    for (i=str.length-1; i>=0; i--){
        revStr += str[i];
    }
    return revStr;
}

console.log(reverseString2("creature")); // "erutaerc"