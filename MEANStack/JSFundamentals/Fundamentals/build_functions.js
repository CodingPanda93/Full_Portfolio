//Basic: Make a function that can be used anywhere in your file and that when invoked will console.log('I am running!'); Give it the name runningLogger.
function runningLogger() {
  console.log('I am running!');
}
//Basic: Make a function that is callable, has one parameter and multiplies the value of the parameter by 10 before
//returning the result. Give it the name multiplyByTen. Invoke it, passing it the argument 5.
function multiplyByTen(x) {
  var result;
  result = 10 * x;
  console.log(result);
}
multiplyByTen(5);
//Basic: Write two functions (stringReturnOne and stringReturnTwo) that each return a different hard-coded string
function stringReturnOne() {
  console.log("I am one string!");
}
function stringReturnTwo() {
  console.log("I am another string!");
}
stringReturnOne();
stringReturnTwo();
//Medium: Write a function named caller that has one parameter.
//If the argument provided to caller is a function (typeof may be useful), invoke the argument. Nothing is returned.

function caller(x) {
  if (typeof x =='function'){
    console.log ("It's a function!");
    stringReturnTwo();
  }
  else {
    console.log("Not a Function!");
  }
}
caller(stringReturnTwo);
//Medium: Write a function named myDoubleConsoleLog that has two parameters,
//if the arguments passed to the function are functions, console.log the value that each, when invoked, returns.
function myDoubleConsoleLog(x,y) {
  if (typeof x =='function' && typeof y =='function'){
    console.log(x());
    console.log(y());
  }
}
