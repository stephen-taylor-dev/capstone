// License for Timer Functionality Code
// Copyright (c) 2022 by David Powell (https://codepen.io/davidpowell/pen/VaNvgw)

// Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

// The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.



var timer;

var timerCurrent;

var timerFinish;

var timerSeconds;

function drawTimer(percent){

    $('div.timer').html('<div class="percent"></div><div id="slice"'+(percent > 50?' class="gt50"':'')+'><div class="pie"></div>'+(percent > 50?'<div class="pie fill"></div>':'')+'</div>');

    var deg = 360/100*percent;

    $('#slice .pie').css({

        '-moz-transform':'rotate('+deg+'deg)',

        '-webkit-transform':'rotate('+deg+'deg)',

        '-o-transform':'rotate('+deg+'deg)',

        'transform':'rotate('+deg+'deg)'

    });

    $('.percent').html(Math.round(percent)+'%');

}

function stopWatch(){

    var seconds = (timerFinish-(new Date().getTime()))/1000;

    if(seconds <= 0){

        drawTimer(100);

        clearInterval(timer);

        $('input[type=button]#watch').val('Start');

        alert('Finished counting down from '+timerSeconds);

    }else{

        var percent = 100-((seconds/timerSeconds)*100);

        drawTimer(percent);

    }

}

$(document).ready(function(){
    $('#watch').click();

    $('input[type=button]#percent').click(function(e){

        e.preventDefault();
        drawTimer($('input[type=text]#percent').val());

    });

    $('input[type=button]#size').click(function(e){

        e.preventDefault();

       // $('.timer').css('font-size',$('input[type=text]#size').val()+'px');

    });
    
    $('.time').click(function(e){
        var time = this.value;
        var outputTime = time/60;
        $('#timer-time').html(outputTime + ' min. ' + '<i class="bi bi-clock-history"></i>');
        $('#watch').click(function(e){

            e.preventDefault();
    
            if($('#watch').val() == 'Start'){
    
                $('#watch').val('Stop');
    
                timerSeconds = time;
    
                timerCurrent = 0;
    
                timerFinish = new Date().getTime()+(timerSeconds*1000);
    
                timer = setInterval('stopWatch()',50);
    
            }else{
    
                $('#watch').val('Start');
    
                clearInterval(timer);
    
            }
    
        });
    });

    

    

});
