const mongoose = require('mongoose');
const { Schema } = mongoose;
const friendSchema = new Schema ({
  first_name: {
    type: String,
    minlength: 2,
    trim: true,
    required: true,
  },
  last_name: {
    type: String,
    required: true,
    trim: true,
  },
  birthday: {
    type: Date,
    trim: true,
    minlength: 3
  }, {
    timestamps: true
  }
});

module.exports = mongoose.model('Friend', friendSchema);
