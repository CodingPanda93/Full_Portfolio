angular.module('app')
  .factory('userFactory', ['$http', function($http){
    var factory = {};

    factory.users = [];

    factory.createUser = function(user){
      factory.user.push(user)
    };

    factory.getCustomizeUsers = function(callback) {
      $http.get('/users')
        .then(function(response){
          console.log(response);
          factory.users = response.data
          callback(factory.users)
        })
        .catch(function(errorResponse){
          console.log(errorResponse);
        })
    };
    factory.getUsersList = function(callback) {
      $http.get('/list')
        .then(function(response){
          console.log(response);
          factory.users = response.data
          callback(factory.users)
        })
        .catch(function(errorResponse){
          console.log(errorResponse);
        })
    };
    return factory;
  }])
