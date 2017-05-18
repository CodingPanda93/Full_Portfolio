angular.module('app')
  .factory('ninjaFactory',['$http', function($http){
    var factory = {};

    factory.getNinjas = function(callback){
      $http.get('/ninjas')
        .then(function(response) {
          factory.ninjas = response.data;
          callback(factory.ninjas);
        })
        .catch(function(errorResponse) {
          console.log(errorResponse)
        });
    };
    factory.updateNinja = function(ninja, callback) {
      $http.put('/ninjas/' + ninja._id, ninja)
        .then(function(response){
          var index = factory.ninjas.indexOf(ninja);
          //~ evaluates the truthiness
          if (~index) {
            factory.ninajs.splice(index, 1, response.data);
          }
          callback();
        })
        .catch(function(error){
          console.log(error);
        });

    };

    factory.deleteNinja = function(ninja, cb) {
      $http.delete('/ninjas' + ninja._id)
        .then(function(response){
          var index = factory.ninjas.indexOf(ninja);

          if (~index) {
            factory.ninjas.splice(index, 1);
          }
          cb();
        })
        .catch(function(error){
          console.log(error)
        });
    };

    factory.getNinja = function(id, callback) {
      var ninja = factory.ninjas.find(function(ninja){
        return ninja.id === id;
      });

      if (ninja) {
        return callback(null, ninja);
      }

      $http.get('/ninjas/' + id)
        .then(function(response){
          callback(response.data.error, response.data.ninja);
        })
        .catch(function(errorResponse){
          console.error(errorResponse)
        })
    };

    factory.ninjas = [];
    //create function with the first parameter of the data from the controller and the callback to the database
    factory.create = function(ninja, callback) {
      //post path and data we are passing to the database
      $http.post('/ninjas', ninja)
        .then(function(response.data) {
          factory.ninjas.push(response.data);
          //callback information to the controller
          callback();
        })
        .catch(function(error){
          console.log(error);
        })
    }

    return factory;
  }]);
