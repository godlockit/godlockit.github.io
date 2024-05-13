let l10 = document.getElementById("l10")
let btn = document.getElementById("btn")
let num = ["10","25","50","75","100"];

let a = setInterval(()=>{
    for(let i = 0;i<5;i++){
      l10.innerHTML = num[i]  
    }
    
    if (num[i] > 99){
        clearInterval (a)
    }
},1000)




