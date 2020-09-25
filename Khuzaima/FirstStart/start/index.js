/** 
DOM - Document Object Model -> Your screen window in a broswer. Your html, css, and javascript are displayed here.

jQuery is a Javascript library. Makes it easier to target/select and the manipulate DOM.
    $('') - Selector
    Functions built into jQuery
     - .css()
     - .text()
     - .html()
    Event functions built into jQuery
     - .click()
     - .blur()
     - .change()

Javascript is a language to manipulate the DOM and to handle events.
    Ex. Page Load | Login | Click | Scroll | Navigate to different page | Form Submission | Dynamic Content

    var - variables are containers for data | Ex. var name = 'khuzaima';
        - Instantiation -> You need the var keyword to activate (instantiate) your variable

    Primative Data Types - Holds only one piece of data of a certain type
        - Integers -> Whole Numbers Ex. 25
        - Strings -> Any Character | Numbers | Letters w/ quotes. 
        - Boolean -> true or false values | Useful for conditions

    var age = 15;           // Integer
    var color = "black";    // String
    var isRed = false;      // Booleans

    Data Structure - Containers for multiple pieces of data
        - Array -> A list of data | Ex. var names = ['apples', 'bannana', 'grapes'];
            .length() - Gives you number of items in the array | Ex. names.length -> 2
            .push() - Adds items to an array | Ex. names.push('grapes');

            index - Where an item is in the array | starts with 0
            names[0] -> 'apples'
            names[1] -> 'bannana'


   --------- BASIC PROGRAMMING ---------
    Closures - Little blocks of code surrounded by brackets
    Each of the following items have closures: 
        - functions
        - if statements
        - loops

    Functions are blocks of code that does tasks
        function() {
            // You put tasks here
        }

    if statements | Conditional statements
        if (condition) {
            // Do these items
        } else if (condtion) {
            // Do these items
        } else {
            // Do these items
        }

    Looping - A circle going back to the same spot
        Ex. var cars = ['toyota', 'honda', 'ford'];
            var currentCar = cars[1];
            $('h1').text(currentCar);

         ------- Visualization -------
        cars.length -> Number of items in cars list -> 3

        Round 1 
            i = 0;
            i < cars.length | 0 < 3? -> Yes

            Do stuff inside loop
            Add 1 to i 
        Round 2
            i = 1
            i < cars.length | 1 < 3? -> Yes

            Do stuff inside loop
            Add 1 to i 
        Round 3
            i = 2
            i < cars.length | 2 < 3? -> Yes

            Do stuff inside loop
            Add 1 to i 
        Round 4
            i = 3
            i < cars.length | 3 < 3? -> No
            Exit Loop
            
        for (var i=0; i < cars.length; i++;) {
            // What you are going to do with the loop
        }







 * */ 