angular.module("app", ['ngRoute'])
  .config(['$routeProvider', function($routeProvider){
    $routeProvider
      .when('/animals', {
        templateUrl: 'partials/animals/_index.html',
        controller: 'animalsController'
      })
      //add a new animal to list
      .when('/animals/new', {
        templateUrl: 'partials/animals/_new.html',
        controller: 'animalsController'
      })
      //show animal
      .when('/animals/:id', {
        templateUrl: 'partials/animals/_show.html',
        controller: 'animalsController'
      })
  }])
