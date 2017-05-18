const Friend = require('mongoose').model('Friend');

module.exports = {
  index: function(request, response) {
    Friend.find({})
      .then(function(friends) {
        response.json(friends);
      })
      .catch(function(error){
        response.status(502).json({error: error});
      });
  },
  create: function(request, response) {
    Friend.create(request.body)
      .then(function(friend){
        response.json(friend);
      })
      .catch(function(error){
        response.status(502).json({error: error});
      });
  },
  show: function(request, response) {
    Friend.findbyId(req.params.id, (error, friend) => {
      if (error) {
        response.status(502).json({error: error});
      } else {
        response.json(friend);
      }
    })
  },
  update:  function(request, response) {
    Friend.findbyIdAndUpdate(request.params.id, request.body, {new: true})
      .then(function(friend){
        response.json(friend);
      })
      .catch (function(error){
        response.status(502).json({error: error});
      })
  },
  destroy: function(request, response) {
    Friend.findbyIdAndRemove(request.params.id)
      .then(function() {
        response.json()
      })
      .catch (function(error){
        response.status(502).json({error: error});
      })
  }
}
