'use strict';

var mongoose = require('mongoose'),
    Thing = mongoose.model('Thing'),
    Notifications = mongoose.model('Notifications'),
    Test = mongoose.model('Test');

/**
 * Get awesome things
 */
exports.awesomeThings = function(req, res) {
  return Thing.find(function (err, things) {
    if (!err) {
      return res.json(things);
    } else {
      return res.send(err);
    }
  });
};


/**
 * Get test stuff
 */
exports.test = function(req, res) {
  return Test.find(function (err, things) {
    if (!err) {
      return res.json(things);
    } else {
      return res.send(err);
    }
  });
};


/**
 * Get notifications  stuff
 */
exports.notifications = function(req, res) {
  // return Notifications.find(function (err, things) {
  //   if (!err) {
  //     return res.json(things.slice(0,5));
  //   } else {
  //     return res.send(err);
  //   }
  // });
  Notifications.find({}).sort({"timestamp": 1}).limit(6).exec(function(err, result) {
      if (err) {
          console.log('sad face');
      } else {
          res.json(result);
      }
  });

};
