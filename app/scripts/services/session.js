'use strict';

angular.module('pinboardApp')
  .factory('Session', function ($resource) {
    return $resource('/api/session/');
  });
