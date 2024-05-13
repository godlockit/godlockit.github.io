// let input = document.querySelectorAll("#ol")

let car2 = document.querySelector(".car2")
let ol1 = document.querySelector("#ol1")
let ol2 = document.querySelector("#ol2")


function lol(){
        if (ol1.checked == true){
            car2.style.opacity = 1
        }
        else if(ol1.checked == false){
            car2.style.opacity = 0
            if(ol2.checked == true){
                car2.style.opacity = 1
                
            }
            else{
                car2.style.opacity = 0
            }
        }
        else{
            console.log("seccesful")
        }
}
