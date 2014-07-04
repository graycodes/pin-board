'use strict';

var mongoose = require('mongoose'),
  User = mongoose.model('User'),
  Test = mongoose.model('Test'),
  Notifications = mongoose.model('Notifications'),
  Thing = mongoose.model('Thing');

/**
 * Populate database with sample application data
 */

//Clear old things, then add things in
Thing.find({}).remove(function() {
  Thing.create({
    name : 'HTML5 Boilerplate',
    info : 'HTML5 Boilerplate is a professional front-end template for building fast, robust, and adaptable web apps or sites.',
    awesomeness: 10
  }, {
    name : 'AngularJS',
    info : 'AngularJS is a toolset for building the framework most suited to your application development.',
    awesomeness: 10
  }, {
    name : 'Karma',
    info : 'Spectacular Test Runner for JavaScript.',
    awesomeness: 10
  }, {
    name : 'Express',
    info : 'Flexible and minimalist web application framework for node.js.',
    awesomeness: 10
  }, {
    name : 'MongoDB + Mongoose',
    info : 'An excellent document database. Combined with Mongoose to simplify adding validation and business logic.',
    awesomeness: 10
  }, function() {
      console.log('finished populating things');
    }
  );
});


Test.find({}).remove(function() {
  Test.create({
    this : 'Something'
  }, function() {
      console.log('finished populating test');
    }
  );
});

Notifications.find({}).remove(function() {
  Notifications.create({
      title: "Low on coffee",
      body: "We've liek, totally run out.",
      timestamp: new Date(),
      author: "Hungover guy"
    },
    { "title" : "High on coffee", "body" : "Iiiii dddrraannkk sssooo mmuucchhh ccooffeee.", "timestamp" : "2014-07-04T09:09:37.776Z", "author" : "Buzzzzinngg"},
    {
      title: "Foosball tournament",
      body: "Foosball tournament starting at some point, because we like foosball and we think you do too. The winner will get some kind of paper crown to wear.",
      timestamp: "2014-07-04T09:09:39.776Z",
      author: "that guy"
    },/*{
      title: "Low on coffee",
      body: "We've liek, totally run out.",
      timestamp: new Date(),
      author: "Hungover guy"
    },*/
    function() {
      console.log('finished populating notes');
    }
  );
});

// Clear old users, then add a default user
User.find({}).remove(function() {
  User.create({
    provider: 'local',
    name: 'Test User',
    email: 'test@test.com',
    password: 'test'
  }, function() {
      console.log('finished populating users');
    }
  );
});
