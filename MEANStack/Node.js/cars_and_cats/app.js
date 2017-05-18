// get the http module:
var http = require('http');
// fs module allows us to read and write content for responses!!
var fs = require('fs');
// creating a server using http module:
var server = http.createServer(function (request, response){
  //define image variables
    var img = null;
    var type;
    if (request.url === '/images/mustang.jpg') {
        img = `.${request.url}`;
        type = 'image/jpg';
    } else if (request.url === '/images/camaro.jpg') {
        img = `.${request.url}`;
        type = 'image/jpg';
    } else if (request.url === '/images/jeep.jpg') {
        img = `.${request.url}`;
        type = 'image/jpg';
    } else if (request.url === '/images/focus.jpg') {
        img = `.${request.url}`;
        type = 'image/jpg';
    } else if (request.url === '/images/king.jpg') {
        img = `.${request.url}`;
        type = 'image/jpg';
    } else if (request.url === '/images/black_cat.jpg') {
        img = `.${request.url}`;
        type = 'image/jpg';
    } else if (request.url === '/images/strange.jpg') {
        img = `.${request.url}`;
        type = 'image/jpg';
    }
    // see what URL the clients are requesting:
    console.log('client request URL: ', request.url);
    // Have localhost:7077/cars go to a simple HTML page that shows some cool pictures of different cars.
    // These car pictures should be stored in your images folder on your server.
    if(request.url === '/cars') {
        fs.readFile('views/cars.html', 'utf8', function (errors, contents){
            response.writeHead(200, {'Content-Type': 'text/html'});  // send data about response
            response.write(contents);  //  send response body
            response.end(); // finished!
        });
    }
    else if (img != null) {
        fs.readFile(img, function(errors, contents){
            response.writeHead(200, {'Content-type': `${type}`});
            response.write(contents);
            response.end();
        });
    }
    else if(request.url === '/stylesheets/styles.css'){
        fs.readFile('./stylesheets/styles.css', 'utf8', function(errors, contents){
            response.writeHead(200, {'Content-type': 'text/css'});
            response.write(contents);
            response.end();
        });
    }
    //Have localhost:7077/cats show a simple HTML page with some cool pictures of cats.
    //Again, make sure these pictures are stored on your server.
    else if (request.url === "/cats") {
         fs.readFile('views/cats.html', 'utf8', function (errors, contents){
             response.writeHead(200, {'Content-type': 'text/html'});
             response.write(contents);
             response.end();
         });
    }
    //Have localhost:7077/cars/new show a simple form where the user can add a new car information
    else if (request.url === "/cars/new") {
         fs.readFile('views/newcar.html', 'utf8', function (errors, contents){
             response.writeHead(200, {'Content-type': 'text/html'});
             response.write(contents);
             response.end();
         });
    }
    // request didn't match anything:
    else {
        response.writeHead(404);
        response.end('URL Request is Not Available!');
    }
});
// tell your server which port to run on
server.listen(7707);
// print to terminal window
console.log("Running in localhost at port 7707");
