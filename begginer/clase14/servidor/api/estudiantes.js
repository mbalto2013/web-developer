var express = require("express");
var mongoose = require("mongoose");
var router = express.Router();

var Estudiante = require("../schemas/estudiante.js");

router.get("/", function(req, res) {
  Estudiante.find().exec()
    .then(
      function(result) {
        res.json(result);
      }
    );
});

router.post("/insertar", function(req, res) {
	var estudianteNuevo = new Estudiante({
	  _id: new mongoose.Types.ObjectId(),
	  nombre: req.body.nombre,
	  carrera: req.body.carrera,
	  edad: req.body.edad
	});
	estudianteNuevo.save()
	  .then(
		function(result) {
		  res.json(result);
		}
	  );
  });
  
  router.post("/buscar", function(req, res) {
	var idUsuario = req.body.idUsuario;
	Estudiante.findById(idUsuario).exec()
	  .then(
		function(result) {
		  res.json(result);
		}
	  );
  });


module.exports = router;