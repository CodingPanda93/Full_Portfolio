function whatHappensToday() {
  var chance = Math.trunc(math.random()*100) + 1;
    if (chance <=10) {
      return "VOLCANO!";
    }
    else if (chance <=25) {
      return "TSUNAMI!";
    }
    else if (chance <= 45) {
      return "EARTHQUAKE!";
    }
    else if (chance <= 70) {
      return "BLIZZARD!";
    }
    else if (chance <= 100) {
      return "METEOR!";
    }
console.log(WhatHappensToday())
}
