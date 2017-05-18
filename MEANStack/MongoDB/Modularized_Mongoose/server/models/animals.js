var mongoose = require('mongoose');

var AnimalSchema = new mongoose.Schema({
 animal: {type: String},
 age: {type: String},
 num_of_legs: {type: Number}
}, {timestamps: true})

mongoose.Promise = global.Promise;
var Animal = mongoose.model('Animal');
