const Ninja = require('mongoose').model('Ninja');

module.exports = {
  index: function(request, response) {
    Ninja.find({})
    .then(function(ninjas) {
      response.json(ninjas);
    })
    .catch(function(error){
      response.status(502).json( { error: error });
    });
  },
  show: function(request, response) {
    Ninja.findbyId(request.params.id, (error, ninja) => {
      console.log('in ninja.findbyid')
      if (error) {
        return response.status(502).json({error: error});
      }

      response.json({error:!ninja, ninja});
    })
  },
  create: function(request, response) {
    Ninja.create(request.body)
      .then(function(ninja){
        response.json(ninja);
      })
      .catch(function(error){
        response.status(502).json({error: error});
      });
  },
  update: function(request, response) {
    Ninja.findbyIdAndUpdate(request.params.id, request.body, { new: true })
      .then(function(ninja) {
        response.json(ninja);
      })
      .cath(function(error){
        response.status(502).json({error: error});
      })
  },
  destroy: function(request, response) {
    Ninja.findbyIdAndRemove(request.params.id)
      .then(function(ninja) {
        response.json(true);
      })
      .catch(function(error){
        response.status(502).json({error: error});
      });
  },
}
