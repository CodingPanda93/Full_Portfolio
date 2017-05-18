//Create a function that takes in one parameter called “name” and returns an object that looks similar to the person object from JS Fundamentals Part II.
function personConstructor(name){
  var person = {
    name: name,
    distance_traveled: 0,
    //say_name - should alert the object’s name property
    say_name: function(){(console.log(person.name))},
    //say_something - have it accept a parameter. This function should then say for example “{{your name}} says ‘I am cool’” if you pass ‘I am cool’ as an argument to this method.
    say_something: function(x) {
      console.log(person.name, "says", x)
    },
    //walk - have it alert for example “{{your name}} is walking” and increase distance_traveled by 3
    walk: function(){
      alert(person.name, 'is walking');
      distance_traveled += 3;
    },
    //run - have it alert for example “{{your name}} is running” and increase distance_traveled by 10
    run: function(){
      alert(person.name, 'is running');
      distance_traveled += 10;
    },
    //crawl - have it alert for example “{{your name}} is crawling” and increase distance_traveled by 1
    crawl: function(){
      alert(person.name, 'is crawling');
      distance_traveled += 1;
    }
  }
  person.say_name();
}
personConstructor('Henry');
