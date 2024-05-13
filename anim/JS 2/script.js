let a = ["+79668435234","awgasjhf@mail.ru",9,"SDKFGHOARNMGLwrnjghioqwhgkpnjbiqehrbipjaerbljqerhipwejlgjwOPYHWPIHWPBMWENJGKHEA;RAERK;GMdmv",]
let btn = document.querySelector(".btn")
let h = document.querySelectorAll("#horns")
btn.addEventListener("click", ()=>{
    let name = document.getElementById("name")
    name.value = "vafel";
    tel.value = a[0];
    email.value = a[1];
    age.value = a[2];
    sel.value = "Men"
    nos.value = "GG"
   for(let i of h){
    i.checked = true
   }
})

