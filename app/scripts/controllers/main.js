'use strict';

angular.module('pinboardApp')
    .controller('MainCtrl', function MainCtrl($scope, NotificationFactory) {
        
        this.notifications = NotificationFactory.notifications;

        this.getNotifications = function() {
            NotificationFactory
                .getNotifications()
                .then(function() {
                    this.notifications = NotificationFactory.notifications;
                    console.log(this.notifications);
                    console.log(this);
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
