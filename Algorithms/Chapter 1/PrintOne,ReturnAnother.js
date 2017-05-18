var arr =[];
var odd = 0;
var secondtolast = 0;

for (var i = 0; i<arr.length; i++){
  if (arr[i] % 2 === 1) {
    odd = arr[i];
  }
  if (arr[i] === arr[arr.length -1]){
    arr[i] = secondtolast;
  }
}
console.log(secondtolast);
return(odd);
