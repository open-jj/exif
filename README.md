# tools

Tools is a repository that has free tools that anyone can use for their tasks.

[website](http://vklyucheno.xyz) for bookmarklets and other stuff.

## WORDLE
Put this into your searchbar for the wordle tool and remove the $:
``javascript:{const d=new Date("June 21, 2021 11:59:00"),g=d.getTime(),f=Date.now(),h=f-g,j=h/864e5,o=Math.round(j),k=o+1;let xmlHttpReq=new XMLHttpRequest;xmlHttpReq.open("GET","https://raw.githubusercontent.com/vklyucheno/tools/main/wordle/words.txt",!1),xmlHttpReq.send(null),n=xmlHttpReq.responseText,m=n.split(/\n|\r/g),alert("Today's wordle is "+m[k]+".");}``
