'use strict';

var mongoose = require('mongoose'),
    Test = mongoose.model('Test');

/**
 * Get awesome things
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
