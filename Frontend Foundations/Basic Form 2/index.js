console.log("test");

/**
 * HTML - Building Blocks of Content
 * CSS - DESIGN
 * JS - UI ACTIONS | Frontend/ Backend Communication
 * jQuery -> Select Items on the DOM for alteration
 */


// Event Handlers
// Click | Blur | Change | Scroll

// Modification Functions
// CSS
// Adds HTML/ Removes HTML
// Loading Data | .ajax() -> Connect to Backend
// .css() | .text() | .val() | .append()



// $() - Selector | Selects your html

$('.form').css({'background-color':'green'});
console.log($('.form').css('background-color'));

$('h1').text('HELLO THERE!');

$('h1').append('<button>CLICK ME MARIO!</button><p>Its a me luigi</p>');



// Click Function
// Submit Button | Background color gets changed of the submit button
// Callback Functions

var colors = ['red', 'yellow', 'purple', 'blue'];

$('#submitBtn').off().on('click', function() {
    var randomNum = Math.floor(Math.random() * 3);
    console.log(randomNum);
    var randomColor = colors[randomNum];
    console.log(randomColor);
    $('#submitBtn').css({'background-color':randomColor});
});


