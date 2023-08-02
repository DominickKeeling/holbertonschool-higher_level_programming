#!/usr/bin/node
/*
Write a script that computes and prints a factorial
The first argument is integer(argument can be cast as integer) used
for computing the factorial
Factorial of NaN is 1
You must do it recursively
You must use a function
*/

const myArgs = process.argv.slice(2);
if (isNaN(myArgs[0])) {
  console.log('%i', 1);
} else {
  console.log(factorial(myArgs[0]));
}

function factorial (x) {
  return (x !== 1) ? x * factorial(x - 1) : 1;
}
