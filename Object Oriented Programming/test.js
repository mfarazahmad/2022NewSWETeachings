

/**
 * Kalid 
 * REST API - Python
 * HTML, Java, JS
 * 
 * Hamza
 * HTML, CSS, JS, Python, SQL
 * 
 * 
 * Practice Foundations
 */






// Submit
$('button').click(function() {
    // Do Actions

    var name = $('.name').val();
    var contact = $('contact').val();
    var desc = $('desc').val();

    var payload = {'name': name, 'contact': contact, 'desc':desc};

    // Ajax - Goal: Send my payload to the backend so I can save it
    $.ajax({
        method: 'POST',
        url: '/saveContact',
        data: payload,
        headers: 'content-type:application/json',
        success: function(response) {
            console.log(response);
        },
        error: function() {

        }
        }
    );

});