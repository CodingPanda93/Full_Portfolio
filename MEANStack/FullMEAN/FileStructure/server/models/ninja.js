const mongoose = require('mongoose');
const { Schema } =  mongoose;
const ninjaSchema = new Schema ({
  name: {
    type: String,
    minlength: 2,
    required: true,
    trim: true,
  },
  location: {
    type: String,
    required: true,
    trim: true,
  },
  belt: {
    type: Schema.Types.ObjectId, ref:'Belt'
  }
} , {
  timestamps: true
});

module.exports = mongoose.model('Ninja', ninjaSchema);
