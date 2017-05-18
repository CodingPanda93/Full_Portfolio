var mongoose = require('mongoose');
var Users = require('./../controllers/users.js');

//Restful routes
module.exports = (function(app){
  app.get('/users', Users.index);
  app.get('/users/:id', Users.show);
  app.post('/users', Users.create);
  app.put('/users/:id', Users.update);
  app.delete('/users/:id', Users.delete);

  app.post('/login', Users.login);
  app.post('/register', Users.register);
})
