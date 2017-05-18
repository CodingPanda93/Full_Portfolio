const express = require("express");
const path = require("path");
// create the express app
const app = express();
// static content
app.use(express.static(path.join(__dirname, "./static")));
// setting up ejs and our views folder
app.set('views', path.join(__dirname, './views'));
app.set('view engine', 'ejs');
// root route to render the index.ejs view
app.get('/', function(req, res) {
 res.render("index", {count: 0});
})
// this selects our port and listens
// note that we're now storing our app.listen within
// a variable called server. this is important!!
const server = app.listen(6789, function() {
 console.log("listening on port 6789");
});
var io = require('socket.io').listen(server);
io.sockets.on('connection', function (socket){
    socket.on('epic_button', function (data){
      io.sockets.emit('update_count')
    })
    socket.on('reset_button', function (data){
      io.sockets.emit('reset_count')
    })
  })
}
