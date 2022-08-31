
document.addEventListener('DOMContentLoaded', function() {
    const user_id = JSON.parse(document.getElementById('user_id').textContent);
    
    // Liturgy Length Button Action
    document.querySelectorAll('.time').forEach(timeButton => {
        timeButton.addEventListener('click', function() {
            const liturgyLength = timeButton.value  
            console.log(liturgyLength)
            // Makes a POST request to the server to get requested liturgy data
            // Runs the like view on the backend
            fetch(`/liturgy/${liturgyLength}`)
            .then(response => response.json())
            .then(data => {
                document.querySelector("#liturgy-title").innerHTML = `<i class="bi bi-book"></i> ` + data.title;
                document.querySelector("#liturgy-author").innerHTML = "by " + data.author;
                document.querySelector("#liturgy-text").innerHTML = data.text;
                document.querySelector("#prev-button").value = data.id - 1;
                document.querySelector("#next-button").value = data.id + 1;
                document.querySelector("#liturgy-id").innerHTML = "About " + data.length + " min.";

            })  

        })
    })

    // Prev and Next Button Actions
    document.querySelectorAll('.navigate').forEach(navigateButton => {
        navigateButton.addEventListener('click', function() {
            var liturgyID = navigateButton.value
            const nextButton = document.querySelector("#next-button");
            var totalLiturgies = nextButton.getAttribute("data-value1");
            liturgyID = parseInt(liturgyID);
            totalLiturgies = parseInt(totalLiturgies);
            
            if (totalLiturgies >= liturgyID && liturgyID > 0) { 
                // Makes a request to the server to get requested liturgy data
                fetch(`/liturgy-navigate/${liturgyID}`)
                .then(response => response.json())
                .then(data => {
                    console.log(data)
                    document.querySelector("#liturgy-title").innerHTML = `<i class="bi bi-book"></i> ` + data.title;
                    document.querySelector("#liturgy-author").innerHTML = "by " + data.author;
                    document.querySelector("#prev-button").value = data.id - 1;
                    // if (liturgyID  == totalLiturgies){
                        
                    //}
                    document.querySelector("#next-button").value = data.id + 1;
                    document.querySelector("#liturgy-id").innerHTML = "About " + data.length + " min.";
                    document.querySelector("#text-block").innerHTML = '<p id="liturgy-text" class="lead">' + ${data.text} + '</p>';
                })
            }  
            else  {
                alert("No more previous or next liturgys in database")
            }    


        })
    })


    // Favorite Liturgy Button
    document.querySelectorAll('#favorite-liturgy').forEach(favoriteButton => {
        favoriteButton.addEventListener('click', function() {
            const favoriteButton = document.querySelector("#favorite-liturgy")
            const liturgyID = favoriteButton.getAttribute("data-value1")
            //const liturgyID = favoriteButton.value

            // Makes a POST request to the server to get requested liturgy data
            // Runs the like view on the backend

            fetch("/liturgy-favorite", {
                method: 'POST',
                body: JSON.stringify({
                    // records who liked the post. based on the user logged in
                    //user: request.user.id,
                    liturgy: liturgyID
                })
                
            })
            .then(response => response.json())
            .then(data => {
                // Send back the new like count and display on the page

            })  

        })
            

        })

        // Switch group buttons
        document.querySelectorAll('.groups').forEach(groupButton => {
        groupButton.addEventListener('click', function() {
            
            // if group menu option clicked id is number, switch user to that group
            // if create group, pop up that menu
            // if invite gropu pop up that menu
            // if manage group pop up that menu

            const groupID = groupButton.value
            const currentGroupID = document.querySelector("#chooseGroupButton").value
            // Makes a POST request to the server to get requested liturgy data
            // Runs the like view on the backend
            if (parseInt(groupID) != parseInt(currentGroupID)) {
                fetch("/switch-groups", {
                    method: 'POST',
                    body: JSON.stringify({
                        // records who liked the post. based on the user logged in
                        //user: request.user.id,
                        group: groupID
                    })
                    
                })
                .then(response => response.json())
                .then(data => {
                    console.log(data.group.name)
                    // Send back the new like count and display on the page
                    console.log("it worked!")
                    document.querySelector("#chooseGroupButton").innerHTML = "Your Group: " + data.group.name;

                })  
            }
            


        })
    })

    // Invite people to groups
    inviteButton = document.querySelector('#sendGroupInvite');
    inviteButton.addEventListener('click', function() {
            const recipients = document.querySelector('#invite-recipients').value;
            const group = inviteButton.getAttribute("data-value1")
            console.log(recipients)
            fetch("/send-invite", {
                method: 'POST',
                body: JSON.stringify({
                    // records who liked the post. based on the user logged in
                    //user: request.user.id,
                    recipients: recipients,
                    group: group
                    
                })
                
            })
            .then(response => response.json())
            .then(data => {
                console.log("sent invites")

            })  

        })
            




})