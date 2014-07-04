'use strict';

var mongoose = require('mongoose'),
    Schema = mongoose.Schema;
    
/**
 * Test Schema
 */
var TestSchema = new Schema({
  this: String
});

/**
 * Validations
 */
// TestSchema.path('awesomeness').validate(function (num) {
//   return num >= 1 && num <= 10;
// }, 'Awesomeness must be between 1 and 10');

mongoose.model('Test', TestSchema);
