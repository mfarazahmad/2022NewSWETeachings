// Javascript - A language that modifies the page based on events. | Modify Elements | Animations | Sending/Loading Data
// jQuery - A library in javascript that selects an element, and lets you change.

// Two Parts | 1. Selector | 2. jQuery Function

// Selector - $("") -> Put an html element, class or id in the paranthesis.
// You can also put the this keyword that lets you select a particular element

// jQuery Functions -> .css() | .text() | .val()
// jQuery Event Functions -> .click() | .change()


//---------------------------------------------------------------------------

// 1. For the characters left to be displayed for the email field
//     - $(".characterCount") - Select the element you want
//     - .text() - Puts text into that element
//     - Javascript variable to keep track of whats in the element.

$("input[name='email']").change( 
    function () {
        var emailValue = $("input[name='email']").val(); 
        var emailLength = emailValue.length;

        var charactersLeft = 15 - emailLength;
        $(".characterCount").text(charactersLeft); 
    }
);

// 2. When you click submit an alert box pops up with the values inside the form.

$("button").click(function() {
    var firstName = $("input[name='firstName']").val();
    var lastName = $("input[name='lastName']").val();
    var email = $("input[name='email']").val();
    var discovery = $("input[name='discovery']").val();

    alert("The first name is " + firstName + "\n lastname is" + lastName + "\n email is " + email + "\n discovery is " + discovery);
    
});
