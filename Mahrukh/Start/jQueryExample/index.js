// When clicking goal titles, description appears
$("h3").click(function() {
    $(this).parent().find("p").css({'display':'block'});
});

// Whilst clicking on a picture, the picture appears bigger
$("img").click(function() {
   $(this).css({'height': '200px', 'width':'200px'}); 
});

//When clicking on the title, title color changes from black to blue
$("h1").click(function(){

    var currentClass = $(this).attr('class');        //blackHeader
    console.log(currentClass);

    if (currentClass === 'blackHeader' ) {
        $(this).removeClass('.blackHeader').addClass('.redHeader');
    } else {
        $(this).removeClass('.redHeader').addClass('.blackHeader');
    }

});


