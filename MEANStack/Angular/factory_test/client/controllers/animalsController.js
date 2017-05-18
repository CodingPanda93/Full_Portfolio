angular.module('app')
  .controller('animalsController', ['$scope', 'animalFactory' function($scope, animalFactory){
    $scope.animals = animalFactory.getAnimals();

    $scope.addAnimal = function() {
      //create animal
      $scope.animals.push($scope.animal);
    }
    $scope.getAnimals = function() {
      //get all animals
      $scope.animals = animalFactory.getAnimals();
    }
    $scope.getAnimal = function(){
      //show one animal
    }
  }])
