//var os = require('os');
//console.log(os.platform());
//console.log(os.arch());
//console.log("Hola");
var express = require('express'); // Incluyo express
var path = require('path'); // Incluyo path
var app = express(); // Inicializo Express
var folder = path.join(__dirname, 'public_html'); // Defino el path del website
app.use(express.static(folder)); // Le indico que use el path del website
app.listen(5090, function(){ // Levanto servidor
  console.log("Servidor corriendo en puerto 5090");
});
