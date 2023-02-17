let i = 0;

let images = [];

let transition_time = 5000;

images[0] = "/static/img/711-frs.jpg";

images[1] = "/static/img/harrison-black-white.jpg";

images[2] = "/static/img/frs-gas.jpg";


function slideshow(){
    let car = document.getElementById('car-img');
    car.src = images[i]

    if ( i < images.length - 1){
        i ++;
    }

    else{
        i = 0;
    }

    setTimeout("slideshow()", transition_time);
}

window.onload = slideshow;