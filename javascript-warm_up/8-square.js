#!/usr/bin/node
/*
Write a script that prints a square
The first arg is the size of the square
fi the first arg cant be converted to an integer print "missing size"
Must use the character X to pritn the square
must use a loop
*/

const myArg = process.argv.slice(2);

if (isNaN(myArg[0])) {
  console.log('Missing size');
} else {
  let myStr = '';
  for (let x = 0; x < myArg[0]; x++) {
    myStr += 'X';
  } for (let y = 0; y < myStr.length; y++) {
    console.log(myStr);
  }
}
