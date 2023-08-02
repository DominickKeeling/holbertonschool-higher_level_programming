#!/usr/bin/node
/*
Write a script that prints the addition of 2 integers
The first argument is the first integer
The second argument is the second integer
You have to define a function with this prototype: function add(a, b)
*/

const myArgs = process.argv.slice(2);
if (isNaN(myArgs[0]) || isNaN(myArgs[1])) {
  console.log('NaN');
} else {
  console.log(add(myArgs[0], myArgs[1]));
}

function add (a, b) {
  return +a + +b;
}
