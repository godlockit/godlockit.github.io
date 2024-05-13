let clot = document.getElementById("clot");
let btn = document.getElementById("btn");

btn.addEventListener("click",()=>{
    let hex_num = ["1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"];
    let hexcode = "";
    let hexcode2 = "";
    
    for(let i = 0; i<6;i++){
        let random_index = Math.floor(Math.random()*hex_num.length);
        hexcode +=hex_num[random_index];

    }
    for(let i = 0; i<6;i++){
        let random_index = Math.floor(Math.random()*hex_num.length);
        hexcode2 +=hex_num[random_index];

    }
    
    clot.innerHTML = hexcode;
    document.body.style.background = "#"+hexcode;
    btn.style.background = "#" + hexcode;
    btn.style.borderColor = "#" + hexcode2;
    
    main.style.borderColor="#"+ hexcode2;
})
let po = document.getElementById("po");

while(true){
    for(let i = 0; i<6;i++){
        let hex_num = ["1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"];
        let hexcode3 = "";
        let random_index = Math.floor(Math.random()*hex_num.length);
        hexcode3 +=hex_num[random_index];
    }
    po.style.color ="#" + hexcode3;
    
    
}