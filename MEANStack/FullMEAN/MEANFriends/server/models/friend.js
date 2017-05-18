const mongoose = require('mongoose');
const { Schema } = mongoose;
const friendSchema = new Schema ({
  first_name: {
    type: String,
    minlength: 2,
    required: true,
    trim: true,
  },
  last_name: {
    type: String,
    minlength: 2,
    required: true,
    trim: true,
  },
  birthday: {
    type: Date,
    required: true,
    trim: true,
  }
}, { timestamps: true});

module.exports = mongoose.model('Friend', friendSchema);
