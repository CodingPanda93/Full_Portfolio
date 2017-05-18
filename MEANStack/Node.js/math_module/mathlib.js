module.exports = function (){
  return {
    add: function(num1, num2) {
        console.log("The sum is:", num1 + num2);
    },
    multiply: function(num1, num2) {
         console.log("The result of multiplication:", num1 * num2);
    },
    square: function(num) {
         console.log("This number squared:", num * num);
    },
    random: function(num1, num2) {
         console.log("A random number between", num1, "and", num2, "is:", Math.floor(Math.random() * ((num2-num1)+1) + num1));
    }
  }
};
