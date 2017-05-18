function Deck(){
  //When constructor function is invoked, run this code
  this.buildDeck();
}

Deck.prototype.buildDeck = function () {
  var suit = ['hearts', 'diamonds', 'spades', 'clubs'],
      value = ['Ace','King','Queen','Jack', '10', '9', '8', '7', '6', '5', '4', '3', '2'],
      self = this;
  this.cards = [];
  //Populate deck with cards
  suits.forEach(function(suit){
    values.forEach(function(value){
      self.cards.push(new Card(value, suit));
    });
  });
  return this;
}
Deck.prototype.shuffle = function() {
  var unshuffled = this.cards.length, temp, i;
  // While there remain elements to shuffle…
  while (unshuffled) {
    // Pick a remaining element…
    i = Math.floor(Math.random() * m--);
    // And swap it with the current element.
    temp = cards[unshuffled];
    cards[unshuffled] = cards[i];
    cards[i] = temp;
  }
  return array;
}

Deck.prototype.reset = function() {
  this.cards = new Deck()
}
Deck.prototype.dealRandomCard= function() {

}
//Whenever a card is selected or dealt it has the following parameters to make a card (value/suit)
function Card(value, suit) {
  this.value = value;
  this.suit = suit;
}
function Player(name){
  this.name = name;
  this.hand = [];
}
Player.prototype.takeCard = function() {

}
Player.prototype.discard = function() {

}
