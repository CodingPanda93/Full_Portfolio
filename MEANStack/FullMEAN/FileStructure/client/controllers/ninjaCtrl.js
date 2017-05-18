angular.module('app')
  .controller('ninjaCtrl',
    ['$scope', 'ninjaFactory', '$location' '$routeParams'
      function($scope, ninjaFactory, $location, $routeParams){
        $scope.ninjas = []


        $scope.getNinjas = function() {
          ninjaFactory(function(ninjas){
            $scope.ninjas = ninjas;
          });
        };

        $scope.getNinja = function() {
          var ninja = $scope.ninjas.find(function(ninja){
            ninja._id === $routeParams.id;
          });
          if (ninja) {
            $scope.ninja = ninja;
          }
          else {
            ninjaFactory.getNinja($routeParams.id, function(error, ninja){
              if (error) {
                return console.error(error);
              }

              $scope.ninja = ninja;
            });
          }
        };

        $scope.updateNinja = function() {
          ninjaFactory.updateNinja($scope.ninja, function(){
            $location.path("/ninjas/" + $scope.ninja._id)
          });
        };

        $scope.delete = function() {
          nf.deleteNinja(ninja, function(){
            //display message
          });
        };

        $scope.create = function() {
          ninjaFactory.create($scope.ninja, function(){
            //once you create an ninja, go back to ninjas index
            $location.path('/ninjas');
          });
        }
      }
    }
  ]
);
