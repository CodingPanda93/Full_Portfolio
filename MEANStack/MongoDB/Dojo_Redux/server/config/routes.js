var quotes = require('../controllers/quotes.js');
module.exports = function(app) {
  app.get('/', function(req, res) {
      // This is where we will retrieve the users from the database and include them in the view page we will be rendering.
      res.render('index');
  })
  app.get('/quotes', function(req, res){
    // Logic to grab all quotes and pass into the rendered view
    quotes.show(req, res)
  });
  app.post('/quotes', function(req, res){
    quotes.create(req, res)
  });
}
}
