document.addEventListener('DOMContentLoaded', function() {
    
    // Prayer Length Button Action
    document.querySelectorAll('.time').forEach(timeButton => {
        timeButton.addEventListener('click', function() {
            const prayerLength = timeButton.value  
            // Makes a POST request to the server to get requested prayer data
            // Runs the like view on the backend
            fetch(`/prayer/${prayerLength}`)
            .then(response => response.json())
            .then(data => {
                document.querySelector("#prayer-title").innerHTML = `<i class="bi bi-book"></i> ` + data.title;
                document.querySelector("#prayer-author").innerHTML = "by " + data.author;
                document.querySelector("#prayer-text").innerHTML = data.text;
                document.querySelector("#prev-button").value = data.id - 1;
                document.querySelector("#next-button").value = data.id + 1;
                document.querySelector("#prayer-id").innerHTML = "About " + data.length + " min.";

            })  

        })
    })

    // Prev and Next Button Actions
    document.querySelectorAll('.navigate').forEach(navigateButton => {
        navigateButton.addEventListener('click', function() {
            var prayerID = navigateButton.value
            const nextButton = document.querySelector("#next-button");
            var totalPrayers = nextButton.getAttribute("data-value1");
            prayerID = parseInt(prayerID);
            totalPrayers = parseInt(totalPrayers);
            
            if (totalPrayers >= prayerID && prayerID > 0) { 
                // Makes a request to the server to get requested prayer data
                fetch(`/prayer-navigate/${prayerID}`)
                .then(response => response.json())
                .then(data => {
                    document.querySelector("#prayer-title").innerHTML = `<i class="bi bi-book"></i> ` + data.title;
                    document.querySelector("#prayer-author").innerHTML = "by " + data.author;
                    document.querySelector("#prev-button").value = data.id - 1;
                    // if (prayerID  == totalPrayers){
                        
                    //}
                    document.querySelector("#next-button").value = data.id + 1;
                    document.querySelector("#prayer-id").innerHTML = "About " + data.length + " min.";
                    document.querySelector("#prayer-text").innerHTML = data.text;})
            }  
            else  {
                alert("No more previous or next prayers in database")
            }    


        })
    })


    // Favorite Prayer Button
    document.querySelectorAll('#favorite-prayer').forEach(favoriteButton => {
        favoriteButton.addEventListener('click', function() {
            const favoriteButton = document.querySelector("#favorite-prayer")
            const prayerID = favoriteButton.getAttribute("data-value1")
            //const prayerID = favoriteButton.value
            console.log(prayerID)  
            // Makes a POST request to the server to get requested prayer data
            // Runs the like view on the backend

            fetch("/prayer-favorite", {
                method: 'POST',
                body: JSON.stringify({
                    // records who liked the post. based on the user logged in
                    //user: request.user.id,
                    prayer: prayerID
                })
                
            })
            .then(response => response.json())
            .then(data => {
                // Send back the new like count and display on the page

            })  

        })
            

        })


})