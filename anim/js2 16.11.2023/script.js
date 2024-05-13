let clot = document.getElementById("clot");
let btn = document.getElementById("btn")

btn.addEventListener("click", ()=>{
    let object = {
        "Флоренс Найтингейл": '"Своим успехом я обязана тому, что никогда не оправдывалась и не принимала оправданий от других"',
        "Майкл Джордан" : '"За свою карьеру я пропустил более 9000 бросков, проиграл почти 300 игр. 26 раз мне доверяли сделать финальный победный бросок, и я промахивался. Я терпел поражения снова, и снова, и снова. И именно поэтому я добился успеха."',
        "Амелия Эрхарт" : '"Сложнее всего начать действовать, все остальное зависит только от упорства."',
        "Федор Достоевский":'"Надо любить жизнь больше, чем смысл жизни."',
        "Альберт Эйнштейн" :'"Логика может привести Вас от пункта А к пункту Б, а воображение — куда угодно."'
    };
    let key = Object.keys(object);
    let aftor = key[Math.floor(Math.random()*key.length)];
    let citata = object[aftor];
    h1.innerHTML = "- " + aftor;
    p.innerHTML = citata;
})

    let p = document.createElement("p");
    let h1 = document.createElement("h1");
    clot.appendChild(h1)
    clot.appendChild(p)







