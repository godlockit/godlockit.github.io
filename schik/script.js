let second = document.getElementById("seconds");
let tens = document.getElementById("tens");
let star = document.getElementById("start");
let st = document.getElementById("stop");
let reset = document.getElementById("reset");
let i = 0;
let s = 0;
let interval 

star.addEventListener("click",()=>{
    clearInterval (interval)
        interval = setInterval(start,10);
});



st.addEventListener("click",()=>{
    clearInterval (interval)
});

reset.addEventListener("click",()=>{
    restart()
})

function restart(){
    tens.innerHTML= "00"
    second.innerHTML = "00"
    clearInterval (interval)
}
function start() {
    s++
    tens.innerHTML = s
    if (s == 100){
        i++;
        s = 0;
        second.innerHTML = i;   
    }
}