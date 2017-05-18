var mongoose = require('mongoose');
    express = require('express');
    app = express();
    bodyParser = require('body-parser');
    path = require('path');
// This is how we connect to the mongodb database using mongoose -- "basic_mongoose" is the name of
//   our db in mongodb -- this should match the name of the db you are going to use for your project.
mongoose.connect('mongodb://localhost/basic_mongoose');
var AnimalSchema = new mongoose.Schema({
 animal: {type: String},
 age: {type: String},
 num_of_legs: {type: Number}
}, {timestamps: true})
mongoose.model('Animal', AnimalSchema); // We are setting this Schema in our Models as 'User'
// Use native promises
mongoose.Promise = global.Promise;
var Animal = mongoose.model('Animal'); // We are retrieving this Schema from our Models, named 'User'
// Integrate body-parser with our App
app.use(bodyParser.urlencoded({ extended: true }));
// Setting our Static Folder Directory
app.use(express.static(path.join(__dirname, './static')));
// Setting our Views Folder Directory
app.set('views', path.join(__dirname, './views'));
// Setting our View Engine set to EJS
app.set('view engine', 'ejs');
// Routes
// Root Request: Display all Animals with route index
app.get('/', function(req, res) {
  // Logic to grab all animals and pass into the rendered view
  Animal.find({}, function(err, results){
    if(err) { console.log(err); }
    res.render('index', { animals: results });
    });
  });
//Display form to make new animals
app.get('/mongooses/new', function(req, res){
  res.render('new');
});
//Action attribute for form, adds new animal
app.post('/mongooses', function(req, res){
  Animal.create(req.body, function(err){
    if(err) { console.log(err); }
    res.redirect('/');
  });
});
app.get('/mongooses/edit/:id', function(req, res){
  //Edit - show form to edit existing animal
  Animal.find({ _id: req.params.id }, function(err, response) {
    if (err) { console.log(err); }
    res.render('edit', { animal: response[0] });
  });
});
app.post('/mongooses/:id', function(req, res){
  Animal.update({ _id: req.params.id }, req.body, function(err, result){
   if (err) { console.log(err); }
   res.redirect('/');
 });
});
app.post('/mongooses/destroy/:id', function(req, res){
  //delete by id
  Animal.remove({ _id: req.params.id }, function(err, result){
   if (err) { console.log(err); }
   res.redirect('/');
 });
});
app.listen(8000, function() {
    console.log("listening on port 8000");
})
