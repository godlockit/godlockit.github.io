let int = document.getElementById("int")
let eys = document.querySelector(".eys")

eys.addEventListener("click" , ()=>{
    if (int.type === "password") {
        int.type = "text"
        eys.src = "show.png"
    }
    else {
        int.type = "password"
        eys.src = "hide.png"
    }
    
})
