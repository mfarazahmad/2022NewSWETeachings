

// We want ot add HTML Elements to the Page Using Javascript

// this | .parent() | .find()

// Modification Function: .text() | .html() | .append() | .val() | .css()
// Event Handler Functions: click() | change()

// CONTENT
// Calculator - Form
// Input Boxes | Add Subtract Multi Division Operators | And Numbers
// Button
// A total section at the bottom that will display total

/** 

[ADD]

_________5________                ___________+__________               _______7___      Total:          

_________7________                ___________*__________               _______2___      Total:          


*/

// DESIGN 
// Flexbox | Centered | Certain Size | Spacing

// LOGIC
//  When you put numbers in the Boxes it performs math and displays total

// CONTENT CODE

var counter = 1;

function generateRow(counter) {
    var row =   '<div class="inputRow">' +
                    `<div><input type="text" placeholder="first number" class="firstNum" id="firstNum${counter}"></div>` +
                    `<div><input type="text" placeholder="operator"     class="operator" id="operator${counter}" ></div>` +
                    `<div><input type="text" placeholder="second number"  class="secondNum" id="secondNum${counter}" ></div>` +
                    `<div><p class="total" id=total${counter}>Total:<span></span></p></div>` +
                '</div>';

    return row;
}

function setupDesign() {
    $('div').css({'margin':'10px'});
    $('.inputRow').css({'display':'flex', 'flex-direction': 'row', 'justify-content':'center', 'align-items':'center'});
}

// BUSINESS LOGIC
$('body').off().on('change', 'input', function () {
    // I either need to figure out my counter value
    var id = $(this).attr("id");        // This is a JS keyword that refers in jQuery to the element that invoked the function

    // I need a way to identify the particular input that is running this
    console.log($(this));

    var inputRowSelector = $(this).parent().parent();

    var firstNum =  parseInt(inputRowSelector.find('.firstNum').val());
    var operator = inputRowSelector.find('.operator').val();
    var secondNum = parseInt(inputRowSelector.find('.secondNum').val());

    if (operator === '+')  {
        var total = firstNum + secondNum;
    } else if  (operator === '-')  {
        var total = firstNum - secondNum;
    } else if  (operator === '*')  {
        var total = firstNum * secondNum;
    } else if  (operator === '/')  {
        var total = firstNum / secondNum;
    } else {
        var total = "Error";
    }

    inputRowSelector.find('.total').css({'color':'red'});
    inputRowSelector.find('.total').text(total);
});

// Event Handlers ONLY track what exists on the page at the time of creation
// Using .off() and .on() WITH a parent element allows you to bypass this

var firstRow = generateRow(1);
$('body').append('<div><button>ADD</button></div>');
$('body').append(firstRow);

// DESIGN CODE
$('body').css({'height':'100vh', 'width':'100vw'});
$('body').css({'display':'flex', 'flex-direction': 'column', 'justify-content':'center', 'align-items':'center'});
setupDesign();

$('button').click(function() {
    counter += 1;
    console.log(counter);
    var newRow = generateRow(counter);
    $('body').append('<div class="line" style="background:red"></div>')
    $('.line').css({'border':'1px solid black', 'height': '3px', 'width': '100%' });
    $('body').append(newRow);
    setupDesign();
});


