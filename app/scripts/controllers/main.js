'use strict';

angular.module('pinboardApp')
    .controller('MainCtrl', function ($scope, $http) {
        $http.get('/api/notifications').success(function(notifications) {
            $scope.notifications = notifications;
        });

    });
