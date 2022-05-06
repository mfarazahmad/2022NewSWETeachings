
// ---------PURE JAVASCRIPT--------

// ---------Function Examples-------
function getNames() {
 // What you want to happen goes here
}

getNames();


// ------ PRIMATIVE DATA TYPES ------ 
var name = 'Khuzaima';      // String
var age = 15;               // Integer
var cash = 15.0             // Float

// ------ DATA STRUCTURES ------ 

// Array  - List container for Data
var students = [];                              // Initializing an array
students.push('Yusuf');                         // Pushing data into an array
var firstStudent = students[0];                 // Gets the first index in the array and puts it in a variable

var name;                                       // Initializing a varible - Defining a variable without assigning it anything

var testScores = [85, 100, 75, 51];
console.log(testScores[2]);


// ------ CONDITIONAL STATEMENTS ------ 
/* Conjunction words - Can be used to combine muliple condition
        and has && for
        or has || for
    Javascript uses one = for assignment. Ex. var name = 'Khuzaima.
    3 === signs are used for comparison.
    > greater than
    < less than
    != not equal
*/

if (testScores[2] >= 70) {
    console.log('Good job you passed!')
} else if (testScores[2] < 70 && testScores[2] > 40) {
    console.log('You passed');
} else {
    console.log('You failed');
}

/*
if (condition) {
    // What happens when condition passes
} else if (condtion) {
    // Condition 2
}
*/


// ------ LOOPS ------ 
/* 
    Iterative - They are used to repeat the same logic mulitple times
    for (var counter=0; //condtion with counter; counter++ ) {
        // What logic you want to repeat
    }

    while (condition) {
         // What logic you want to repeat
    }
*/

var altTestScores = [55, 84, 33, 95];
// if they have between 70 to 100 passes
// if they dont fails


// if my grade altTestScores[1]
// is less than 100 and greater than 70
// tell them you psased


for (var i=0; i < altTestScores.length; i++ ) {
    console.log("Counter is: " + i);
    console.log("Test score is:" + altTestScores[i]);

    if (altTestScores[i] < 100 && altTestScores[i] > 70) {
        console.log("Great Job");
    } else {
       console.log("You failed");
    }

}









