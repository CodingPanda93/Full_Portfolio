const mongoose = require('mongoose');
const { Schema } = mongoose;
const beltSchema = new Schema({
  name: {
    type: String,
    required: true,
    trim: true,
    unique: true,
    lowercase: true
  },
  level: {
    type: Number,
    required: true,
    unique: true,
    min: 1,
    max: 10
  }
}, {
  timestamps: true
});

module.exports = mongoose.model('Belt', beltSchema);
