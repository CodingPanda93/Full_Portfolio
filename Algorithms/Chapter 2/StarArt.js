function drawleftStars(num){

var chars = ' '
while(chars.length < 75) {
  if (chars.length < num) {
    chars += "*"
  }
  else {
    chars =+ "_"
  }
}
console.log(chars)
}
