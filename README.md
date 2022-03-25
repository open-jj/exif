# tools

Tools is a repository that has free tools that anyone can use for their tasks.

[website](http://vklyucheno.xyz) for bookmarklets and other stuff.

## WORDLE
Put this into your searchbar for the wordle tool:
``javascript:const e=new Date("June 21, 2021");var t=e.getTime(),t=(Date.now()-t)/864e5,t=Math.round(t)+1;let o=new XMLHttpRequest;o.open("GET","https://raw.githubusercontent.com/vklyucheno/tools/main/wordle/words.txt",!1),o.send(null),n=o.responseText,m=n.split(/\n|\r/g),alert("Todays wordle is "+m[t]+".")'``
