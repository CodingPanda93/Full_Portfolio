//Go through each value in the array x, where x = [3,5,"Dojo", "rocks", "Michael", "Sensei"]. Log each value.
var x;
x = [3,5,"Dojo", "rocks", "Michael", "Sensei"];
for (var i = 0; i < x.length; i++) {
  console.log(x[i]);
}
//Add a new value (100) in the array x using a push method.
x.push(100);
//Add a new array ["hello", "world", "JavaScript is Fun"] to variable x. Log x in the console and analyze how x looks now.
x.push(["hello", "world", "JavaScript is Fun"])
console.log(x)
//Create a simple for loop that sums all the numbers between 1 to 500. Have console log the final sum.
var y;
var sum;
y = 0;
sum = 0;
while (y < 501) {
  sum = sum + y;
  y--;
}
console.log(sum);
//Write a loop that will go through the array [1, 5, 90, 25, -3, 0], find the minimum value, and then print it
var array;
array = [1, 5, 90, 25, -3, 0];
var min = array[0];
for (var i = 1;i < array.length; i++)  {
  if (min > array[i]){
    min = array[i];
  }
  else {
      continue
  }
}
console.log(min);
//Write a loop that will go through the array [1, 5, 90, 25, -3, 0], find the average of all of the values, and then print it
var array2;
array2 = [1, 5, 90, 25, -3, 0];
var avg = 0;
for (var i = 0; i < array2.length; i++){
  avg += array2[i];
}
avg /= array2.length;
console.log(avg);
//Write a for-in loop that will navigate through the object below (or write your own object):
var newNinja = {
 name: 'Jessica',
 profession: 'coder',
 favorite_language: 'JavaScript', //like that's even a question!
 dojo: 'Dallas'
}
for (var key in newNinja) {
  if (newNinja.hasOwnProperty(key)){
    console.log(key);
    console.log(newNinja[key]);
  }
}
