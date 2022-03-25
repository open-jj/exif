javascript:(function(){
    const d = new Date("June 21, 2021");
    const g = d.getTime();
    const f = Date.now();
    const h = f - g;
    const j = h / 86400000;
    const o = Math.round(j);
    const k = o + 1;

    let xmlHttpReq = new XMLHttpRequest();
    xmlHttpReq.open("GET", 'https://raw.githubusercontent.com/vklyucheno/tools/main/wordle/words.txt', false); 
    xmlHttpReq.send(null); 
    n = xmlHttpReq.responseText;
    m = n.split(/\n|\r/g);
    alert("Today's wordle is " + m[k] + ".");
})()
