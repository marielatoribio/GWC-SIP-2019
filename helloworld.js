var adjectives = ["brave","courageous","happy","amazing"];
var pos = 0;

var loc = document.getElementById("adjective")

function changeAdj(){
  loc.innerHTML = adjectives[pos];
  pos ++;
  if (pos >= adjectives.length){
    pos = 0;
  }
}

// Math.random() //[0, 1]
//
// var x = document.getElementsByTagName("body")[0]
// function colorfulBackground(){
//   x = setAltribute("style",'background-color:rgb($(Math.floor(Math.random()* 256)},
//   ${Math.floor(Math.random() * 256)}, ${Math.floor(Math.random() * 256)})')
// }
