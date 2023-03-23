

let i = 0;
let j = 0;
function slideshow(){
    let car_slides = document.getElementsByClassName("car-slide");
    let gundam_slides = document.getElementsByClassName('gundam-slide');
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
    

    if (j < gundam_slides.length - 1){
        gundam_slides[j].style.display = "None";
        j ++;
        gundam_slides[j].style.display = "inline";
    }
    else{
        gundam_slides[j].style.display = "None";
        j = 0;
        gundam_slides[j].style.display = "inline";
    }
    setTimeout(slideshow, 5000)
}
setTimeout(slideshow, 5000)
// window.onload = slideshow;

