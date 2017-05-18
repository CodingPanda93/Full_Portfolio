angular.module('app')
  .factory('animalFactory', function(){
    var factory = {};

    factory.animals = [];

    factory.addAnimal = function(animal) {
      factory.animals.push(animal);
    };

    factory.getAnimals = function() {
      return factory.animals;
    };
    
    return factory;
  });
