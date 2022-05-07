// When the Button is Clicked the info from the form will be shown

// jQuery Library - Select Elements on the DOM and Modify the DOM

// Modification Functions | .text() | .css() | .html() | .append() | .val()
console.log($('h2').text());
$('h2').text("My name is Jeff");

$('#submitBtn').css({'color': 'red'});

console.log($('.formContainer').css('color'));
console.log($('#name').val());

// Event Handler Functions - Click | MouseOn | KeyPress

// Selector should be WHAT is triggering the event
// All event handlers require functions passed in
// When an event is triggered a function gets run

// Call Back Function -> A function that gets run after another function
// Example 1
//$("#submitBtn").click(function() {
//    alert('HEY');
//});

$("#submitBtn").click(function() {
    var name = $("#name").val();
    var email = $("#email").val();
    var message = $("#message").val();

    alert(`The name is: ${name}, the email is: ${email} and the message is: ${message}`);
    $('.formContainer').append(`<li>The name is: ${name}, the email is: ${email} and the message is: ${message}</li>`);
    
    // Connect to Python and send this data there
});