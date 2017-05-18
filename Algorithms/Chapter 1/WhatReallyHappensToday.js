function WhatReallyHappensToday() {

  var events=[];
  function chance (min,max) {
    return Math.floor(Math.random()*(max-min +1))+ min;
  }

    if (chance(1,100) <=10) {
      events.push("VOLCANO!");
    }
    if (chance(1,100) <=25) {
      events.push("TSUNAMI!");
    }
    if (chance(1,100) <= 45) {
      events.push("EARTHQUAKE!");
    }
    if (chance(1,100) <= 70) {
      events.push("BLIZZARD!");
    }
    if (chance(1,100) <= 100) {
      events.push("METEOR!");
    }
console.log(events);
}
}
