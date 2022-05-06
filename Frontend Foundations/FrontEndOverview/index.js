// This is where our Javascript goes

// PRIMITIVE DATA TYPES
// Booleans - True or False | Strings - Alphanumeric in Quotes | Integers - Numbers
var isTrue = true;      // isTrue = True
var name = "Faraz";     // name = "Faraz"
var age = 12;           // age = 12

// DATA STRUCTURES
// Dictionaries | Arrays

var groceries = ['banannas', 'cookies', 'chips'];
console.log(groceries[1]);                  // print(groceries[1])

var car = {'make': 'Toyota', 'model': 'Camry', 'year': 2010};
console.log(car['make']);

if (name === "Jeff") {                          // if name == "Jeff":
    console.log("You fail!");
} else if (name === "Faraz") {
    console.log('You win!');
}

//console.log(student);

// Initizalier | Condition | Iterator Amount
for (var i = 0; i < groceries.length; i++) {    //for i in range(0, len(groceries)):
    console.log(groceries[i]);
}       

function sum(num1, num2) {                      // def sum():
    var total = num1 + num2;
    console.log(total);
}

sum(7, 2);
sum(12, 5);
sum(16, 11);
