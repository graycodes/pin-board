'use strict';

var mongoose = require('mongoose'),
    Schema = mongoose.Schema;
    
/**
 * Notifications Schema
 */
var NotificationsSchema = new Schema({
  title: String,
  body: String,
  timestamp: Date,
  author: String,
  hidden: {
      type: Boolean,
      default: false
  }
});

/**
 * Validations
 */
// NotificationsSchema.path('awesomeness').validate(function (num) {
//   return num >= 1 && num <= 10;
// }, 'Awesomeness must be between 1 and 10');

mongoose.model('Notifications', NotificationsSchema);
