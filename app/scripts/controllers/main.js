'use strict';

angular.module('pinboardApp')
    .controller('MainCtrl', function ($scope, $http) {
        var getStuff = function() {
            console.log('again');
            $http.get('/api/notifications').success(function(notifications) {
                $scope.notifications = notifications;
            });
        };
        setInterval(getStuff, 4000);
        getStuff();

    });
