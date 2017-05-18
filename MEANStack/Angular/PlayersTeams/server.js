const express = require('express');
const path = require('path');
const port = process.env.PORT || 8080;
const parser = require('body-parser');
const app = express();

app.use(express.static(path.resolve('client')));
app.use(express.static(path.resolve('bower_components')));
app.use(parser.json());

app.listen(port, () => console.log(`listening on port ${ port }`));
