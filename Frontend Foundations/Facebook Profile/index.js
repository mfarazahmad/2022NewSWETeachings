/** 
Build FB Profile
- Friends List
- Wall Posts
- Descriptions
*/


console.log('Butt');
var names = ["Faraz", "Ali", "Kamran", "Rakin", "Khuzaima"];

for (var i = 0; i<names.length; i++) {
    $(".friendsList").append(`<li>${names[i]}</li>`);
}

$('.addFriend').click(function() {
    var name = $('.friendName').val();
    $('.friendsList').append(`<li>${name}</li>`);
});


$('.postBtn').click(function() {
    var post = $(".wallInput").val();
    $('.wallPosts').append(`<li>${post}</li>`);
});
