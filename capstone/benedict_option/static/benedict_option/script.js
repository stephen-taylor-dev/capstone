
document.addEventListener('DOMContentLoaded', function() {
    const user_id = JSON.parse(document.getElementById('user_id').textContent);

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
                    document.querySelector("#liturgy-title").innerHTML = `<i class="bi bi-book"></i> ` + data.title;
                    document.querySelector("#liturgy-author").innerHTML = "by " + data.author;
                    document.querySelector("#prev-button").value = data.id - 1;
                    // if (liturgyID  == totalLiturgies){
                        
                    //}
                    document.querySelector("#next-button").value = data.id + 1;
                    //document.querySelector("#liturgy-id").innerHTML = "About " + data.length + " min.";
                    document.querySelector("#text-block").innerHTML = data.text;
                })
            }  
            else  {
                alert("No more previous or next liturgys in database")
            }    
        })
    })


        // Switch group buttons
        document.querySelectorAll('.groups').forEach(groupButton => {
        groupButton.addEventListener('click', function() {
            const groupID = groupButton.value;
            const listGroupsButton = document.querySelector("#listGroupsButton");
            const prevGroupID = listGroupsButton.getAttribute('data-value1');
            const prevGroupName = listGroupsButton.getAttribute('data-value2');
            // Makes a POST request to the server to get requested liturgy data
            // Runs the like view on the backend
            if (parseInt(groupID) != parseInt(prevGroupID)) {
                fetch("/switch-groups", {
                    method: 'POST',
                    body: JSON.stringify({
                        group: groupID
                    })
                })
                .then(response => response.json())
                .then(data => {
                    // Send back the new like count and display on the page
                    listGroupsButton.innerHTML = "Your Current Group: " + data.group.name;
                    listGroupsButton.setAttribute('data-value1', data.group.id);
                    listGroupsButton.setAttribute('data-value2', data.group.name);
                    groupButton.setAttribute('value', prevGroupID );
                    groupButton.innerHTML = `<a class="dropdown-item" href="#">${prevGroupName} </a>`
                    if (window.location.pathname == '/prayer-request') {
                        location.reload();
                    }
                })  
            }
        })
    })


    // Invite people to groups
    inviteButton = document.querySelector('#sendGroupInvite');
    inviteButton.addEventListener('click', function() {
            const recipients = document.querySelector('#invite-recipients').value;
            const group = inviteButton.getAttribute("data-value1");

            fetch("/send-invite", {
                method: 'POST',
                body: JSON.stringify({
                    recipients: recipients,
                    group: parseInt(group)
                    
                })
            })
            .then(response => response.json())
            .then(data => {
                console.log("sent invites")
            })  
        })


    // Create group
    createButton = document.querySelector('#createGroupInvite');
    createButton.addEventListener('click', function() {
            const group = document.querySelector('#createGroupFormName').value;
            fetch("/create-group", {
                method: 'POST',
                body: JSON.stringify({
                    group: group
                })
            })
            .then(response => response.json())
            .then(data => {
                console.log("created group and sent invites")
            })  
        })
            
        
         // Create Comments
         document.querySelectorAll('#create-comment-button').forEach(createCommentButton => {
            createCommentButton.addEventListener('click', function() {
                const commentMessage = document.querySelector('#comment-input').value;
                const pr_id = createCommentButton.getAttribute("data-prid");
                const group = createCommentButton.getAttribute("data-grid");
                fetch("/create-comment", {
                    method: 'POST',
                    body: JSON.stringify({
                        // records who liked the post. based on the user logged in
                        prayer_request: pr_id,
                        message: commentMessage
                    })
                })
                .then(response => response.json())
                .then(data => {
                    console.log("create comment")
                })  
            })
        })

              
        
       
       // Load invite modal 
        document.querySelectorAll('#group-invite').forEach(respondInviteModal => {
            respondInviteModal.addEventListener('click', function() {
                const sender = respondInviteModal.getAttribute('data-value1');
                const group = respondInviteModal.getAttribute("data-value2");
                const date = respondInviteModal.getAttribute("data-value3");
                document.querySelector('#invite-information').innerHTML = `<p class="fs-5" id="invite-information"> ${sender} invited you to the group <strong>${group}</strong> at ${date}</p>`;

            })
                
    
           })
        // Respond to Group Invite
        document.querySelectorAll('.submitResponse').forEach(respondInviteButton => {
            respondInviteButton.addEventListener('click', function() {
                
            invite_data = document.querySelector('#group-invite');
            const inviteID = invite_data.getAttribute('data-value4');
            const groupID = invite_data.getAttribute('data-value5');
            if (respondInviteButton.innerHTML == 'Accept'){
                fetch("/respond-invite", {
                    method: 'PUT',
                    body: JSON.stringify({
                        // records who liked the post. based on the user logged in
                        invitation_id: inviteID,
                        group_id: groupID,
                        accepted: true,
                        delete: false  
                    })
                })
                .then(response => response.json())
                .then(data => {
                    console.log("accepted invitation")
                })  
            }
            else {
                fetch("/respond-invite", {
                    method: 'PUT',
                    body: JSON.stringify({
                        // records who liked the post. based on the user logged in
                        invitation_id: inviteID,
                        accepted: false,
                        delete: true,  
                    })
                })
                .then(response => response.json())
                .then(data => {
                    console.log("deleted invitation")
                })  
            }

            })
        })
                
    
    // // Favorite Liturgy Button
    // document.querySelectorAll('#favorite-liturgy').forEach(favoriteButton => {
    //     favoriteButton.addEventListener('click', function() {
    //         const favoriteButton = document.querySelector("#favorite-liturgy")
    //         const liturgyID = favoriteButton.getAttribute("data-value1")
    //         //const liturgyID = favoriteButton.value

    //         // Makes a POST request to the server to get requested liturgy data
    //         // Runs the like view on the backend
    //         fetch("/liturgy-favorite", {
    //             method: 'POST',
    //             body: JSON.stringify({
    //                 liturgy: liturgyID
    //             })
    //         })
    //         .then(response => response.json())
    //         .then(data => {
    //         })  
    //     })  
    // })


})