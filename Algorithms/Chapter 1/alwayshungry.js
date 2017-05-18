function hungry (arr) {

var arr= [13,[8,4,5],'food',7,true];
var counter=false;
for(var i = 0; i< arr.length; i++){
  if (arr[i] === 'food'){
    console.log('yummy');
    counter = true;
  }
}
if (counter == false){
  console.log("Im hungry!");
}
}
