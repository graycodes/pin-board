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
    Notifications
        .find({"hidden": false})
        .sort({"timestamp": 1})
        .limit(6)
        .exec(function(err, result) {
            if (err) {
                console.log('sad face');
            } else {
                res.json(result);
            }
        });

};
exports.hideNotification = function(req, res) {
    var notificationId = req.params.id;
    var notification = req.body.notification;
    delete notification._id;
    delete notification.__v;

    Notifications
        .update(
            {"_id": mongoose.Types.ObjectId(notificationId)},
            notification
        )
        .exec(function(err, result) {
            if (err) {
                res.write(err);
                console.log('sad face');
            } else {
                res.json(result);
            }
        });

};
