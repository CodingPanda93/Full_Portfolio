var app = angular.module('app', ['ngRoute']);
app.config(function ($routeProvider) {
  $routeProvider
    .when('/new', {
      templateUrl: 'partials/friends/_new.html',
      controller: 'newController',
      controllerAs: 'NC'
    })
    .when('/edit/:_id', {
      templateUrl: 'partials/_edit.html',
      controller: 'editController',
      controllerAs: 'EC'
    })
    .otherwise('/');
});
