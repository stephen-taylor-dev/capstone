

// change play button either to start or pause 
function switch_button() {
    if (document.getElementById("start").innerText == "Pause") {
        document.getElementById("start").className = "btn btn-success";
        document.getElementById("start").innerText = "Start"; 
    } else {
        document.getElementById("start").className = "btn btn-warning";
        document.getElementById("start").innerText = "Pause"; 
    }
}


// reset to default values
function reset() {
    clearInterval(interval);
    switch_button();
    counter = 0; 
    interval = -1;
    document.getElementById("countdown").innerHTML = '';
}

// Function for handling min and sec properly
function convert_time(s) {
    // trunc https://stackoverflow.com/questions/7641818/how-can-i-remove-the-decimal-part-from-javascript-number // 
    // Math to convert secs to minutes. Divide secs by minutes and remove decimal. 
    var min = Math.trunc(s / 60);
    // find secs as remainder 
    var sec = s % 60;
    // https://stackoverflow.com/questions/8935414/getminutes-0-9-how-to-display-two-digit-numbers//
    // format countdown display to have 2 digits.
    return ((min < 10) ? '0' : '') + min + ':' + ((sec < 10) ? '0' : '') + sec;
} 


// create counter variable to count number of secs. elapsed
var counter = 0;
var interval = -1;


// This function executes every time the start/pause button is clicked.
function timer() {
    // convert session min to sec because count_down() will run every sec.
    var minutes = document.getElementById("set_time").value * 60;
    var time = document.getElementById("countdown");
    // Check if timer is paused. If so start count_down again.
    if (interval == -1) {
        // start the countdown interval, calls timer function every sec.
        interval = setInterval(count_down, 1000);
        switch_button();
    
        // Intiates the countdown timer
        function count_down() {
            counter++; 
            // update the countdown display after subtracting min-counter
            time.innerHTML = convert_time(minutes - counter);
            // if the counter = remaining timer has finished
            if (counter == minutes) {
                clearInterval(interval);
                counter = 0;
                time.innerHTML = "Break Time! &#127881;"; 
                // update time in minute input to default to 5 for 5 min break
                document.getElementById("set_time").innerHTML = 5;
                // play alarm sound
                document.getElementById("alarm").play();
            
            }
        }
  
        // Else pause the timer    
    } else {
        clearInterval(interval);
        interval = -1;
        switch_button();
    }  
   
}