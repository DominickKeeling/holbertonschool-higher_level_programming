#!/usr/bin/node
/*
Write a scripts that prints the first argument passed to it:
if no arguments are passed to the script print 'No argument'
you must use console.log(...) to print all output
you are not allowed to use var
you are not allowed to use lengnth
*/

let i = 1;
const values = ['No argument', process.argv[2]];
if (values[1] === undefined) {
  i--;
}
console.log(values[i]);
