angular.module('app')
  .controller('CustomizeUsersController', ['$scope', 'userFactory', function($scope, uF){
    $scope.createUser =  function() {
      $scope.users.push($scope.user)
    };
    $scope.deleteUser = function(id) {
      //where we will delete a user
    };
    $scope.getCustomizeUsers = function() {
      uF.getCustomizeUsers(function(users){
        $scope.users = users;
      });
    };
  }])
