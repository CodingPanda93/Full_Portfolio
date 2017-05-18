//Problem 1
var first_variable;
function firstFunc() {
  var first_variable;
  first_variable = "Not anymore!!!";
  console.log(first_variable);
}
first_variable = "Yipee I was first!";
console.log(first_variable);
firstFunc();

//Problem 2
var food = "Chicken";
function eat() {
  var food;
  food = "half-chicken";
  console.log(food);
  food = "gone";       // CAREFUL!
  console.log(food);
}
console.log(food);
eat();

//Problem 3
var new_word;
function lastFunc() {
  new_word = "old";
  console.log(new_word);
}
new_word = "NEW!";
console.log(new_word);
lastFunc();
