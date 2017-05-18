function VehicleConstructor(name,wheels,passengers) {
  var vehicle = {}; //object being returned
  //properties of vehicle
  vehicle.name = name;
  vehicle.wheels = wheels;
  vehicle.passengers = passengers;
  //methods for vehicle
  vehicle.makeNoise = function() {
    console.log('VROOM VROOM!!');
  }
  return vehicle;
}
//create a Bike
var Bike = VehicleConstructor(Bike,2,1);
//redefine the makeNoise
Bike.makeNoise = function() {
  console.log("Ring Ring!");
}
//create a Sedan
var Sedan = VehicleConstructor(Sedan,4,5);
//redefine the makeNoise
Sedan.makeNoise = function() {
  console.log("Honk Honk!");
}
//create a Bus
var Bus = VehicleConstructor(Bus,4,40);
//Add a method to Bus that takes in the number of passengers to pick up and adds them to the passenger count​
Bus.pickUp = function(num) {
  passengers =+ num;
}
