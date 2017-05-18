function incrementtheSeconds (arr) {

for(var i =1; i<arr.length; i+=2){
    arr[i]++;
  }
}
for(var i=0; i< arr.length; i++){
  console.log(arr[i]);
}
return arr;
}
