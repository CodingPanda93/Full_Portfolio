const friendsController = require('../controllers/friendsController.js');

module.exports = function(app) {
  //CRUD
  app.get('/friends', friendsController.index);
  app.post('/friends', friendsController.create);
  app.put('/friends/:id', friendsController.update);
  app.get('/friends/:id', friendsController.show);
  app.delete('/friends', friendsController.destroy);
}
