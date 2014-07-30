'use strict';

angular.module('pinboardApp')
    .factory('NotificationFactory', function NotificationFactory($http) {

        NotificationFactory.notifications = [];

        NotificationFactory.getNotifications = function() {
            console.log('Loading new data: ' + new Date().toISOString());

            return $http.get('/api/notifications')
                .success(function(data) {
                    NotificationFactory.notifications = data;
            });

        };

        NotificationFactory.deleteNotification = function(index) {
            var notification = NotificationFactory.notifications[index];
            var id = notification._id;

            notification.hidden = true;

            return $http.post('/api/notification/' + id + '/hide/', {notification: notification})
                .success(function(data, status, headers, config) {
                    NotificationFactory.notifications.splice(index, 1);
                }).error(function(data) {
                    console.log('error: ');
                    console.log(data);
                });
        };

        return NotificationFactory;

    });
