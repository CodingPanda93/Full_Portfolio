var app = angular.module('app');

app.controller('editController',['$scope', '$routeParams', 'friendsFactory', function($scope, $routeParams, friendsFactory){
  var self = this;
  self.currentFriend = {}
  var findFriend = function() {
    friendsFactory.getFriend($routeParams._id, function(factoryData){
      self.currentFriend = factoryData;
    });
  }
  findFriend();

  self.update = function() {
    if (!self.currentFriend.name || !self.currentFriend.last_name || !self.currentFriend.birthday){
      console.log('Incorrect or messing information!')
      return;
    }
    friendsFactory.update(self.currentFriend, function(returned_data){
      console.log(return_data);
    });
  }
}]);
