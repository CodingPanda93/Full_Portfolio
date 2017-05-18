const ninjasController = require('../controllers/ninjasController.js');

module.exports = function(app) {
  //CRUD
  app.get('/ninjas', ninjasController.index);
  app.get('/ninjas/:id', ninjasController.show);
  app.post('/ninjas', ninjasController.create);
  app.put('/ninjas/:id', ninjasController.update)
  app.delete('/ninjas/:id', ninjasController.destroy);
};
