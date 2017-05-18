function randomchance () {
var COIN= 23

while (COIN > 0){
 if (Math.trunc(Math.random(Math.random())*100))==(Math.trunc(Math.random(Math.random())*100)){ //Random from 1-100
    COIN = COIN + Math.floor(Math.random()* 50)+51 //How much did she win? IF THEY WON
    }
 else {
   console.log(0);
   COIN--;
 }
}
}
