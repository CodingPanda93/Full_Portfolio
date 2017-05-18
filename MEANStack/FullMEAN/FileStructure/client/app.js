angular.module('app', ['ngRoute'])
  .config(function($routeProvider){
    $routeProvider
      .when('/ninjas', {
        templateUrl: 'partials/ninjas/_index.html',
        controller: 'ninjaCtrl'
      })
      .when('ninjas/:id', {
        templateUrl: 'partials/ninjas/_show.html',
        controller: 'ninjasCtrl'
      })
      .when('/ninjas/new', {
        templateUrl: 'partials/ninjas/_new.html',
        controller: 'ninjaCtrl'
      })
      .when('/ninjas/:id/edit', {
        templateUrl: 'partials/ninjas/_edit.html',
        controller: 'ninjaCtrl'
      })
      .otherwise('/ninjas')
  })
