var app = angular.module('app', []);

app.factory('productFactory', ['$http', function($http) {
        var factory = {};
        var products = [
            {
                name: "hat",
                quantity: 50,
                price: 14.99
            }
        ];
        factory.create = function(data, callback) {
            data.quantity = 50;
            products.push(data);
            callback(products);
        }
        factory.index = function(callback) {
            callback(products);
        }
        factory.update = function(data, callback) {
            if (Number.isInteger(data.quantity)) {
                if (products[data.id].quantity - data.quantity > 0) {
                    products[data.id].quantity -= data.quantity;
                } else {
                    products[data.id].quantity = 0;
                }
            }
            callback(products);
        }
        factory.delete = function(id, callback) {
            products.splice(id, 1);
            callback(products);
        }
        return factory;

    }
])

app.controller('productController', ['$scope', 'productFactory', function($scope, productFactory) {
        // callback, but not as an anonymous function, rather a named function!
        function setProducts(data) {
            $scope.products = data;
            $scope.product = {};
        }

        $scope.product = {};
        $scope.products = [];

        $scope.index = function() {
            productFactory.index(setProducts);
        }

        $scope.index();
        $scope.create = function() {
            productFactory.create($scope.product, setProducts);
        }
        $scope.delete = function(id) {
            productFactory.delete(id, setProducts);
        }

    }
]);

app.controller('ordersController', ['$scope', 'productFactory', function($scope, productFactory) {
        function setProducts(data) {
            $scope.products = data;
            $scope.product = {};
        }
        $scope.products = [];

        productFactory.index(setProducts);
        $scope.update = function(id) {
            productFactory.update({
                id: id,
                quantity: 1
            }, setProducts);
        }
    }
]);
