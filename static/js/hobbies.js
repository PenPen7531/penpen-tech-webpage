let i = 0;

let images = [];

let transition_time = 5000;

images[0] = "/static/img/711-frs.jpg";

images[1] = "/static/img/harrison-black-white.jpg";

images[2] = "/static/img/frs-gas-crop.jpg";


let j = 0;

let gundam = [];

gundam[0] = '/static/img/strike.jpg';

gundam[1] = '/static/img/rx78.jpg';

gundam[2] = '/static/img/strike-freedom.jpg';

gundam[3] = '/static/img/zaku.jpg';

gundam[4] = '/static/img/strike.jpg';

function slideshow(){
    let car = document.getElementById('car-img');
    car.src = images[i]
    let gundam_img = document.getElementById('gundam-img');

    gundam_img.src = gundam[j]  

    if ( i < images.length - 1){
        i ++;
    }

    else{
        i = 0;
    }


    if ( j < gundam.length - 1){
        j ++;
    }

    else{
        j = 0;
    }

    setTimeout("slideshow()", transition_time);
}

window.onload = slideshow;