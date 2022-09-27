document.addEventListener('DOMContentLoaded', function() {
   // Create prayer requests
   createPRequest = document.querySelector('#create-prequest-button');
   createPRequest.addEventListener('click', function() {
       const content = document.querySelector('#prayer-request-input').value;
       fetch("/create-prequest", {
           method: 'POST',
           body: JSON.stringify({
               content: content,
           })
           
       })
       .then(response => response.json())
       .then(data => {
           console.log("Created Prayer Request")

       })  

   })


   
})