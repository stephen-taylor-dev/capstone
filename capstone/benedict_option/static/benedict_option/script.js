document.addEventListener('DOMContentLoaded', function() {
    
    // Like button action
    document.querySelectorAll('.time').forEach(timeButton => {
        timeButton.addEventListener('click', function() {
            const prayerLength = timeButton.value  
            console.log(prayerLength)
            //const prayer = document.querySelector("#prayer").value;
            // 
            // Makes a POST request to the server to the like to the post data
            // Runs the like view on the backend
            fetch(`/prayer/${prayerLength}`)
            .then(response => response.json())
            .then(data => {
                document.querySelector("#prayer-title").innerHTML = `<i class="bi bi-book"></i> ` + data.title
                document.querySelector("#prayer-author").innerHTML = "by " + data.author
                document.querySelector("#prayer-text").innerHTML = data.text
                //prayer = data.text 
                //prayer.innerHTML = data.text;
                // Send back the new like count and display on the page

            })  

        })
    })

})