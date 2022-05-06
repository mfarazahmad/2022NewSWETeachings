
// Event Handlers
// Event - Any Interaction on the Page
// Type | Click | Pop-Up | Click-Away | Hover | Scroll | Load

// Javscript is a language to change things on the page
// Change Design | CSS | HTML

// jQuery - Library | Composition of code someone else wrote to do stuff
// Modify items on the DOM
// DOM - Document Object Model

// Selector - Selects an item on the dom $()
// Action Function - Event Handler | Modification Functions

// Ex.1
$("h1").text("JUICE");
$("button").css({color: 'red'});
$("h1").html("<input>");


// Select Box | Loop through names | Display the names inside green box
var names = ['Rakin', 'Faraz', 'Kamran', 'Ali'];
var listHTML = '';
for (var i = 0; i < names.length; i++) {
    var name = names[i];
    listHTML += `<li> ${name} </li>`;
    console.log(listHTML);
}
$(".box").html(listHTML);

// See if you can get input from the text boxes



