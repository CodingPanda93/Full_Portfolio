var arr= [1,3,5,7,9,13];
var count = 0;
var arrnew= [];

for (var i = 0; i < arr.length; i++){
  if (arr[i] > arr[1]){
    count++;
    arrnew.push(arr[i]);
  }
  if (arr.length = 1) {
    console.log('Nothing to count!')
    break;
  }
}
console.log(count);
console.log(arrnew);
