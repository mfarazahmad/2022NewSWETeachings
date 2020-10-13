/* jQuery is a library to make it easier to 
        1. SELECT items on the DOM (aka html and css)
        2. Lets you MODIFY those elements.

    $() - Selector | HTML elements, classses, or ids go inside paranthesis
    
    Functions
        - Basic Functions
            .css() | .text() | .html() | .val()
        - Event Handler Functions
            .click() | .change() | .scroll()
            Note:   Take in callback function
                    A function that will run once the event is recognized
            
*/

// --------------------------------------------------------

/*
    Our project Actions
    1. Click about and open up about section
    2. You can click reply to add comments
    3. You can see how many characters are left in the comment
    4. Click profile pic to see it larger
    5. Load in friend list
*/

// Load in data from backend
var userName = 'Khuzaima';

// When a page loads I want the user's name to load in
$("#name").text(userName);

// Click about and open up about section
$(".aboutBox").click(function() {
    
    var ele = $(".item");
    var currentDisplay = ele.css('display');

    if (currentDisplay === "none") {
        ele.css({"display": "flex"});
    } else {
        ele.css({"display": "none"});
    }
});


// You can click reply to add comments
$('#addComment').click(function(){
    var comment = $("#commentInput").val();     // "Faraz"
    $('.commentBox').append("<p>" + comment + "</p>")
});

// You can see how many characters are left in the comment
$('#commentInput').change(function() {

    var maxValue = 20;
    console.log(maxValue);
     
    var commentValue = $("#commentInput").val();   // Value in the input box                
    console.log(commentValue);

    var leftOver = maxValue - commentValue.length; 
    console.log(leftOver)

    $('.charactersLeft').text(leftOver);
});


// Click profile pic to see it larger
/*
    - Hint 1: Change CSS WIDTH & HEIGHT to 800px
*/

$('#profilePic img').click(function() {
    var currentHeight = $('#profilePic img').css('height');

    // if currrent height is 150 then change to 800
    if ( currentHeight === '150px') {
        $('#profilePic img').css({"height":"800px", "width":"800px", "position": "absolute"});
    } else {
        $('#profilePic img').css({"height":"150px", "width":"150px", "position": "static"});
    }
});

// Load in friend list
/*
    - Array of Friends & their Profile Pics
    - Loop through each friend
        - Add it to the page
        - Clone existing sample box and insert friend info in it
*/

var friendList = ["hamza", "abid", "faraz", "daniel"];

var pic1 = "https://www.google.com/url?sa=i&url=https%3A%2F%2Funsplash.com%2Fs%2Fphotos%2Fprofile&psig=AOvVaw3ieiMCzb52NEn3DLfpgT5w&ust=1602360808614000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCPDp26mpqOwCFQAAAAAdAAAAABAD";
var pic2 = "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pexels.com%2Fsearch%2Fprofile%2F&psig=AOvVaw3ieiMCzb52NEn3DLfpgT5w&ust=1602360808614000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCPDp26mpqOwCFQAAAAAdAAAAABAN";
var pic3 = "https://www.google.com/url?sa=i&url=https%3A%2F%2Funsplash.com%2Fs%2Fphotos%2Fprofile&psig=AOvVaw3ieiMCzb52NEn3DLfpgT5w&ust=1602360808614000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCPDp26mpqOwCFQAAAAAdAAAAABAS";
var pic4 = "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pinterest.com%2Fpin%2F863846772250682571%2F&psig=AOvVaw3ieiMCzb52NEn3DLfpgT5w&ust=1602360808614000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCPDp26mpqOwCFQAAAAAdAAAAABAX";
var pic5 = "https://www.google.com/url?sa=i&url=https%3A%2F%2Fweheartit.com%2Fpictures%2Fprofile%2520pic&psig=AOvVaw3ieiMCzb52NEn3DLfpgT5w&ust=1602360808614000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCPDp26mpqOwCFQAAAAAdAAAAABAd";

var profileList = [pic1, pic2, pic3, pic4, pic5];

for (var i=0; i<friendList.length; i++) {
    var currentFriend = friendList[i];
    var currentPicture = profileList[i]; 

    var newBox = $("#sampleFriend").clone();    
    $('.friendsContainer').append(newBox);

    var currentBox = $("#sampleFriend").last();
    currentBox.find('.profilePic').attr("src", currentPicture);
    currentBox.find('.friendName').text(currentFriend);
}