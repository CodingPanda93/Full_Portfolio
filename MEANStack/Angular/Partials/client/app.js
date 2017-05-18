angular.module('app', ['ngRoute'])
  .config(['$routeProvider', function($routeProvider){
    $routeProvider
    //when Customize Users is selected then the partial page will show the customization screen
      .when('/users',{
        templateUrl:'partials/users/_customizeUsers.html',
        controller: 'CustomizeUsersController'
      })
    //when User List is selected then the partial page will show partial page for the user list
      .when('/list',{
        templateUrl: 'partials/users/_userList.html',
        controller: 'UserListsController'
      })
      .otherwise('/');
  }]);
