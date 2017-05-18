var mongoose = require('mongoose');
var Animal = mongoose.model('Animal');
module.exports = {
  show: function(req, res) {
    Animal.find({}, function(err, results){
    if(err) { console.log(err); }
    res.render('index', { animals: results });
    });
  },
  create: function (req, res) {
    Animal.create(req.body, function(err){
      if(err) { console.log(err); }
      res.redirect('/');
    });
  },
  edit: function (req, res) {
    Animal.find({ _id: req.params.id }, function(err, response) {
      if (err) { console.log(err); }
      res.render('edit', { animal: response[0] });
    });
  },
  update: function (req, res) {
    Animal.update({ _id: req.params.id }, req.body, function(err, result){
     if (err) { console.log(err); }
     res.redirect('/');
   });
 },
 delete: function (req, res) {
   Animal.remove({ _id: req.params.id }, function(err, result){
    if (err) { console.log(err); }
    res.redirect('/');
  });
 }
}
