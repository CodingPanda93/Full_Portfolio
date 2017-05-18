function VehicleConstructor(name,wheels,passengers,speed) {
  //Private variables
  var self = this;
  var distance_traveled = 0;
  var updateDistance_traveled = function(6) {
    distance_traveled = self.speed * 6;
  }
  var this = {}; //object being returned
  //properties of vehicle
  this.name = name;
  this.wheels = wheels;
  this.passengers = passengers;
  this.speed = speed;
  //methods for vehicle
  this.makeNoise = function() {
    console.log('VROOM VROOM!!');
  }
  this.move = function() {
    updateDistance_traveled();
    makeNoise();
  }
  return this;
}
VehicleConstructor.prototype.checkMiles = function() {
  console.log(this.distance_traveled);
  return this;
}
VehicleConstructor.protype.VIN = Math.floor(Math.random * 10000000);
//create a Bike
var Bike = new VehicleConstructor(Bike,2,1,15);
//redefine the makeNoise
Bike.makeNoise = function() {
  console.log("Ring Ring!");
}
//create a Sedan
var Sedan = VehicleConstructor(Sedan,4,5,50);
//redefine the makeNoise
Sedan.makeNoise = function() {
  console.log("Honk Honk!");
}
//create a Bus
var Bus = new VehicleConstructor(Bus,4,40,40);
//Add a method to Bus that takes in the number of passengers to pick up and adds them to the passenger count​
Bus.pickUp = function(num) {
  passengers =+ num;
}
