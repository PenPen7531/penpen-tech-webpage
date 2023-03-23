

let i = 0;
// document.getElementsByClassName("car-slide")[i].style.display = "inline";
function slideshow(){
    let car_slides = document.getElementsByClassName("car-slide");

    if (i < car_slides.length - 1){
        car_slides[i].style.display = "None";
        i++;
        car_slides[i].style.display = "inline";
    }

    else{
        car_slides[i].style.display = "None";
        i = 0;
        car_slides[i].style.display = "inline";
    }

    setTimeout(slideshow, 5000)
}

window.onload = slideshow;

