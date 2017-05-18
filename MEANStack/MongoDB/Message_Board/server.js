var mongoose = require('mongoose');
    express = require('express');
    app = express();
    bodyParser = require('body-parser');
    path = require('path');
// This is how we connect to the mongodb database using mongoose -- "basic_mongoose" is the name of
//   our db in mongodb -- this should match the name of the db you are going to use for your project.
mongoose.connect('mongodb://localhost/basic_mongoose');
var Schema = mongoose.Schema;
var postSchema = new mongoose.Schema({
 name: {type: String, required: true},
 text: {type: String, required: true },
 comments: [{type: Schema.Types.ObjectId, ref:'Comment'}]
}, {timestamps: true});

var commentSchema = new mongoose.Schema({
  _post: {type: Schema.Types.ObjectId, ref: 'Post'},
  name: {type: String, required: true},
  text: {type: String, required: true},
}, {timestamps: true});
mongoose.model('Post', postSchema);
mongoose.model('Comment', commentSchema);
// store our models in variables
var Post = mongoose.model('Post');
var Comment = mongoose.model('Comment');
// Use native promises
mongoose.Promise = global.Promise;
// Integrate body-parser with our App
app.use(bodyParser.urlencoded({ extended: true }));
// Setting our Static Folder Directory
app.use(express.static(path.join(__dirname, './static')));
// Setting our Views Folder Directory
app.set('views', path.join(__dirname, './views'));
// Setting our View Engine set to EJS
app.set('view engine', 'ejs');
// Routes
app.get('/', function(req, res){
  Post.find({})
  .populate('comments')
  .exec(function(err, posts){
    res.render('index', {posts: posts});
  });
});
app.post('/new_post', function (req, res){
  Post.create(req.body, function(err){
    if(err) { console.log(err); }
    res.redirect('/');
  });
});
app.post("/comment/:id", function(req, res){
	var post_id = req.params.id;
	Post.findOne({_id: post_id}, function(err, post){
		var newComment = new Comment({name: req.body.name, text: req.body.comment});
		newComment._post = post._id;
		Post.update({_id: post._id}, {$push: {"_comments": newComment}}, function(err){
		});
		newComment.save(function(err){
			if(err){
				console.log(err);
				res.render('index.ejs', {errors: newComment.errors});
			} else {
				console.log("comment added");
				res.redirect("/");
			}
		});
	});
});
app.listen(8000, function() {
    console.log("listening on port 8000");
})
