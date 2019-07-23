var adjectives = ["Brave","Happy","Caring","Amazing"];
var pos = 0;

var loc = document.getElementById("adjective")

function changeAdj(){
  loc.innerHTML = adjectives[pos];
  pos ++;
  if (pos >= adjectives.length){
    pos = 0;
  }
}
// this sets the fontsize to increse when (name) is clicked
var sizes = 32
var x = document.getElementsByTagName("h1")[0]
var delta = 10

function bigText(){
  x.setAttribue("style", 'font-size:${size}px')
  size += delta;
  if (size > 92 || size < 32){
  }
}
