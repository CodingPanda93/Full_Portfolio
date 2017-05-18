const express =  require('express');
const app = express();
const parser = require('body-parser');
const path = require('path');

app.use(express.static(path.resolve('client')));
app.use(express.static(path.resolve('bower_components')));

app.user(parser.json());

app.listen(8000, function(){
  console.log('listening on port 8000')
});
