angular.module('app')
  .controller('UserListsController' ['$scope', 'userFactory', function($scope, uF){
    $scope.getUsersList = function() {
      uF.getUsersList(function(users){
        $scope.users = users;
      });
    };
  }])
