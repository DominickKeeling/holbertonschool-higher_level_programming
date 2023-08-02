#!/usr/bin/node
/*
Write a script that prints x times "C is fun"
Where x is the first argument of the script
if the first argument cant be converted to an integer, pritn "Missing number
of occurences"
Must use a loop (while, for, etc)
*/

const input = process.argv[2];

const myArg = process.argv.slice(2);
if (isNaN(myArg[0])) {
  console.log('Missing number of occurrences');
} else {
  for (let x = 0; x < myArg[0]; x++) {
    console.log('C is fun');
  }
}
