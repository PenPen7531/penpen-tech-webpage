

let i = 0;

function slideshow(){
    let car_slides = document.getElementsByClassName("car-slide");
    console.log(car_slides[i])
    console.log(i)
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

