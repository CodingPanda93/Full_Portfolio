//Create a simple for loop that sums all the integers between x and y (inclusive). Have it console log the final sum.
function finalSum(x,y) {
  var sum;
  sum = 0;
  for (var i = x; i < y; i++) {
    sum = sum + i;
  }
  console.log(sum);
}
finalSum(1,500);

//Write a loop that will go through an array, find the minimum value, and then return it
function minArray(arr) {
  var min;
  min = arr[0];
  for (var i = 1; i < arr.length; i++) {
    if (min > arr[i]) {
      min = arr[i];
    }
  }
  console.log(min);
}
minArray([1, 5, 90, 25, -3, 0])
//Write a loop that will go through an array, find the average of all of the values, and then return it
function avgFinder(arr) {
  var avg;
  avg = 0;
  for (var i = 0; i < arr.length; i++){
    avg += arr[i];
  }
  avg /= arr.length;
  console.log(avg);
}
avgFinder([1, 5, 90, 25, -3, 0]);

var object = {
  finalSum: function(x,y) {
    var sum;
    sum = 0;
    for (var i = x; i < y; i++) {
      sum = sum + i;
    }
    console.log(sum);
  },
  minArray: function(arr) {
    var min;
    min = arr[0];
    for (var i = 1; i < arr.length; i++) {
      if (min > arr[i]) {
        min = arr[i];
      }
    }
    console.log(min);
  },
  avgFinder: function(arr) {
    var avg;
    avg = 0;
    for (var i = 0; i < arr.length; i++){
      avg += arr[i];
    }
    avg /= arr.length;
    console.log(avg);
  }
}
object.finalSum(1,500);

var person = {
  name: 'Emily',
  distance_traveled: 0,
  //say_name - should alert the object’s name property
  say_name: function(){(console.log(person.name))},
  //say_something - have it accept a parameter. This function should then say for example “{{your name}} says ‘I am cool’” if you pass ‘I am cool’ as an argument to this method.
  say_something: function(x) {
    console.log(person.name, "says", x)
  },
  //walk - have it alert for example “{{your name}} is walking” and increase distance_traveled by 3
  walk: function(){
    alert('Emily is walking');
    distance_traveled += 3;
  },
  //run - have it alert for example “{{your name}} is running” and increase distance_traveled by 10
  run: function(){
    alert('Emily is running');
    distance_traveled += 10;
  },
  //crawl - have it alert for example “{{your name}} is crawling” and increase distance_traveled by 1
  crawl: function(){
    alert('Emily is crawling');
    distance_traveled += 1;
  }
}
person.say_name()
person.say_something("I am awesome")
