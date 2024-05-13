let img = [
    "p2.jpeg",
    "p1.jpg",
    "1.svg",
    "2.jpg",
    "3.jpeg"
]
let num = 0


slider.src = img[num];
function prev(){
    let slider = document.getElementById("slider");
    num--;
    if(num < 0){
        num=img.length - 1;

    }
    slider.src = img[num];
}
function next(){
    let slider = document.getElementById("slider");
    num++;
    if (num >= img.length){
        num=0;
    }
    slider.src = img[num];
}