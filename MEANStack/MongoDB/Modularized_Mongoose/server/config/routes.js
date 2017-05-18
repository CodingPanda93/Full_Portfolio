var animals = require('../controllers/animals.js');
module.exports = function(app) {
  app.get('/', function(req, res) {
    animals.show(req, res);
  });
  app.get('/mongooses/new', function(req, res){
    res.render('new');
  });
  app.post('/mongooses', function(req, res){
    animals.create(req, res);
  });
  app.get('/mongooses/edit/:id', function(req, res){
    animals.edit(req, res);
  });
  app.post('/mongooses/:id', function(req, res){
    animals.update(req, res);
  });
  app.post('/mongooses/destroy/:id', function(req, res){
    animals.delete(req, res);
  });

}
