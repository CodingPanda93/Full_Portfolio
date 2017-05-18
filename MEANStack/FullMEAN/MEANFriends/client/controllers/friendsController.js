angular.module('app')
  .controller('friendsController',
    ['$scope', 'friendsFactory', '$routeParams', '$location',
      function($scope, friendsFactory, $routeParams, $location){
        $scope.friends = []

        $scope.createFriend = function() {
          friendsFactory.createFriend($scope.friend, function(){
            $location.path('/friends');
          })
        }
        $scope.index = function() {
          friendsFactory.getFriends(function(friends){
            $scope.friends = friends;
          });
        }
        $scope.getFriend = function() {
          friendsFactory.getFriend($routeParams.id, function(friend){
            $scope.friend= angular.copy(friend);
          });
        }
        $scope.updateFriend = function() {
          friendsFactory.updateFriend($scope.friend, function(friend){
            if (error) {
              console.log(error);
              return
            }
            $location.path('/ninjas/' + $scope.friend._id);
          });
        }
        $scope.destroyFriend = function(friend) {
          friendsFactory.destroyFriend(friend, function(error){
            if (error) {
              console.log(error);
            } else {
              $location.path('/friends');
            }
          })
        }
      }
    ]
  );
