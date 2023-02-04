window.onload = async function typeName(){
    alert_view();
    let string = "Hello I am Jeff :) Welcome to My Webpage";

    let display = "";
    let elem = document.getElementById("text");
    console.log(elem.innerHTML);
    for (let i = 0; i < string.length; i++){
        display += string[i]; 
        elem.innerText = display;
        let max = 150;
        let min = 50;
        let delay = Math.floor(Math.random() * (max - min + 1)) + min
        await sleep(delay);
        
        
        
    }
    document.getElementById('content').style.display = "block";
    document.getElementById('nav').style.display = "flex";
    document.getElementById('content').style.animation = "fadeIn 1s linear";
    document.getElementById('nav').style.animation = "fadeIn 1s linear forwards";
}

function sleep(miliseconds){
    return new Promise(resolve => setTimeout(resolve, miliseconds))
}

function add_key(key){
    text = document.getElementById('text').innerHTML

    // if (key == ")" & text.charAt(text.length - 1) == ":"){
    //     text = text.substring(0, text.length - 1);
    //     text += "&#128516";
    //     document.getElementById('text').innerHTML = text;
    //     console.log("change");
    // }
    // else{
        document.getElementById('text').innerHTML += key;
    // }
}

function remove_let(){
    text = document.getElementById('text').innerHTML;
    
    // if (text.substring(text.length - 8, text.length - 1) == "&#128516"){
    //     new_text = text.substring(0, text.length - 8);
    //     console.log("del emeote");
    //     document.getElementById('text').innerHTML = new_text
    // }
    // else{
        new_text = text.substring(0, text.length - 1);

        document.getElementById('text').innerHTML = new_text
    // }
    
}

document.addEventListener('keydown', function(event) {
    const key = event.key; 

    if (key.length == 1){
        add_key(key);
    }

    else if (key == 'Backspace'){
        remove_let();
    }
    
});

window.addEventListener('keydown', function(e) {
    if(e.keyCode == 32 && e.target == document.body) {
      e.preventDefault();
    }
  });

function alert_view(){
    // alert("This webpage will keep track of keyboard presses");
}
