angular.module('app')
  .factory('friendsFactory', ['$http', function($http) {
    var factory = {};

    factory.friends = [
      {first_name: 'Emily', last_name: 'Lint', birthday: '12/13/1993', _id: 1}
    ];

    factory.createFriend = function(friend, callback) {
      $http.post('/friends', friend)
        .then(function(response) {
          factory.friends.push(response.data);
          //callback information to the controller
          callback();
        })
        .catch(function(error){
          console.log(error);
        })
    }
    factory.getFriends = function(callback) {
      $http.get('/friends')
        .then(function(response){
          factory.friends = response.data;
          callback(factory.friends);
        })
        .catch(function(error){
          console.log(error);
        })
    }
    factory.getFriend = function(id, callback) {
      const friend = factory.friends.find(function(friend){
        return friend._id == id;
      })
      if (friend) {
        console.log('Calling Callback');
        callback(friend);
      } else {
        $http.get('/friends/' + id)
          .then(function(response){
            callback(response.data);
          })
          .catch(function(error){
            console.log(error);
          })
      }
    }
    factory.updateFriend = function(friend, callback) {
      $http.put('/friends/' + friend._id, friend)
        .then(function(response){
          var arrFriend = factory.friends.find(function(frien){
            return frien._id === friend._id;
          })
          var index = factory.friends.indexOf(arrFriend);
          factory.friends[index] = response.data;

          callback(null, response.data);
        })
        .catch(callback);
    }
    factory.destroyFriend = function(friend, callback) {
      $http.delete('/friends/' + friend._id)
        .then(function(response) {
          var arrFriend = factory.friends.find(function(frien){
            return frien._id === friend._id;
          })
          var index = factory.friends.indexOf(arrFriend);
          factory.friends.splice(index, 1);

          callback();
        })
        .catch(callback);
    }

    return factory;
  }])
