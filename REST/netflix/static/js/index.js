console.log('Test');

// Save Movies
// When add button is clicked it sends the data to the backend to be saved
$('.addBtn').off().on('click', function() {

    // Collecting the data from the UI form
    var title =  $('.title').val();
    var seasons =  $('.seasons').val();
    var censor =  $('.censor').val();
    var release =  $('.release').val();

    // Adding the new movie to the page
    var movieHTML = '<div class="movies">' +
        `<p>${title}</p>` +
        `<p>${seasons}</p>` +
        `<p>${censor}</p>` +
        `<p>${release}</p>` +
    '</div>';

    // Collect data to send to backend
    var payload = {
        'title': title,
        'seasons': seasons,
        'censorySetting': censor,
        'year': release
    };

    // Send data to backend

    // Ajax is Javascripts way to invoke HTTP
    $.ajax({
        type: "POST",
        url: "/saveMovie",
        data: JSON.stringify(payload),
        dataType: "json",
        contentType: "application/json",
        success: function(resp) {
            alert(resp['msg']);
            $('.moviesList').append(movieHTML);
        },
        error: function(err) {
            console.log(err);
        }
    });
    
});


// Get Movies
// Ajax requires a dictionary with certain keys: type, url, contenttype, success, error

// Requester
$.ajax({
    type: 'GET',
    url: '/getMovies',
    contentType: 'application/json',
    success: function(resp) {
        console.log(resp);

        var moviesList = resp['data'];
        for (var i=0; i < moviesList.length; i++) {

            var currentMovie = moviesList[i];

            var picImage = "https://images.unsplash.com/photo-1503023345310-bd7c1de61c7d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8aHVtYW58ZW58MHx8MHx8&w=1000&q=80"
            
            var newMovie = `<div class="movies" style="background-image: url(${picImage});">` + 
                `<p>${currentMovie['title']}</p>` +
                `<p>${currentMovie['Year']}</p>` +
                `<p>${currentMovie['cast']}</p>` +
                `<p>${currentMovie['censoryRating']}</p>` +
                `<p>${currentMovie['feelings']}</p>` +
                `<p>${currentMovie['title']}</p>` +
                `<p>${currentMovie['UserRating']}</p>` +
                `<p>${currentMovie['genre']}</p>` +
                `<p>${currentMovie['seasons']}</p>` +
            `</div>`;

            $('.moviesList').append(newMovie);
        }
    },
    error: function(err) {
        console.log(err);
    }
});




/** 
 
$('p').css({'color': 'red'});       // Requires a dictionary
$('div').html('<p>Test</p>');       // Requires a string of html
$('testBtn').click(function(){      // Requires a function
    console.log('test');
});

*/