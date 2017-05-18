const mongoose = require('mongoose');
const fs = require('fs');
const path = require('path');

const modelPath = path.resolve('server', 'models');
const jsTest = new RegExp('.js$', 'i');

mongoose.Promise = global.Promise;

mongoose.connect('mongodb://localhost/MEANFriends');
mongoose.connection.on('connected', () => console.log('connected to mongoose'));

fs.readdirSync(modelPath).forEach(file => {
  if(jsTest.test(file)) {
    require(path.join(modelPath, file));
  }
})
