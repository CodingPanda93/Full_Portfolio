angular.module('app', ['ngRoute'])
  .config(function($routeProvider) {
    $routeProvider
      .when('/friends', {
        templateUrl: 'partials/friends/_index.html',
        controller: 'friendsController'
      })
      .when('/friends/new', {
        templateUrl: 'partials/friends/_new.html',
        controller: 'friendsController'
      })
      .when('/friends/:id/edit', {
        templateUrl: 'partials/friends/_edit.html',
        controller: 'friendsController'
      })
      .when('/friends/:id', {
        templateUrl: 'partials/friends/_show.html',
        controller: 'friendsController'
      })
      .otherwise('/')
  })
