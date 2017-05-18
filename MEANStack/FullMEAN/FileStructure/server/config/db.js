const mongoose = require('mongoose');
const fs = require('fs');
const path = require('path');
const modelPath = path.resolve('server', 'models');
const reg = new RegExp('.js$', 'i');

mongoose.connect('mongodb://localhost/ninjasDash');

mongoose.connection.on('connected', () => console.log('mongoose connected'));

fs.readdirSync(modelPath).forEach(model => {
  if (reg.test(model)) {
    require(path.join(modelPath, model));
  }
});
