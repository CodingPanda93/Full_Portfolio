var arr = [];
var low = arr[0];
var high = arr[0];

for (var i = 1; i < arr.length; i++) {
  if (low > arr[i]) {
    low = arr[i];
  }
  if (high < arr[i]) {
    high = arr[i];
  }
}
console.log(low);
return(high);
