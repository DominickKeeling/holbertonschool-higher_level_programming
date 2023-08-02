#!/usr/bin/node
/*
Write a script that searches the second biggest integer in the list of arguments
You can assume all arguments can be converted to integer
If no arguments passed print 0
If the number of arguments is 1, print 0
*/

const myArgs = process.argv.slice(2);
let x = 0;
if (myArgs.length === 0 || myArgs.length === 1) {
  console.log('%i', 0);
} else {
  let largest = -2454635434;
  for (x = 0; x < myArgs.length; x++) {
    if (myArgs[x] > largest) {
      largest = myArgs[x];
    }
  }
  let second = largest;
  for (x = 0; x < myArgs.length; x++) {
    if (myArgs[x] > second && myArgs[x] < largest) {
      second = myArgs[x];
    }
  }
  console.log(second);
}
