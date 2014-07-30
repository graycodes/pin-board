'use strict';

angular.module('pinboardApp')
    .controller('MainCtrl', function MainCtrl(NotificationFactory) {
        
        this.getNotifications = function() {
            NotificationFactory
                .getNotifications()
                .then(function() {
                    this.notifications = NotificationFactory.notifications;
                }.bind(this));
        };

        this.deleteNotification = function(index) {
            NotificationFactory
                .deleteNotification(index)
                .then(function() {
                    this.notifications = NotificationFactory.notifications;
                }.bind(this));
        };

        setInterval(this.getNotifications, 10 * 1000);
        this.getNotifications();

    });
