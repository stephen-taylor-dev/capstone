document.addEventListener('DOMContentLoaded', function() {
    
    // Like button action
    document.querySelectorAll('.time').forEach(timeButton => {
        timeButton.addEventListener('click', function() {
            event.preventDefault();
            // Gets the post id that the user clicked like on
            const prayerTime = timeButton.value  
            // 
            // Makes a POST request to the server to the like to the post data
            // Runs the like view on the backend
            fetch(`/like/${postID}`, {
                method: 'POST',
                body: JSON.stringify({
                    // records who liked the post. based on the user logged in
                    likes: request.user.id
                }),
                headers: {
                    "X-CSRFToken": token
                }
            })
            .then(response => response.json())
            .then(data => {
                // Send back the new like count and display on the page

            })  

        })
    })

})