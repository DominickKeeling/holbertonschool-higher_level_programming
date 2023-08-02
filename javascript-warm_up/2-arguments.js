#!/usr/bin/node
/*
Write a scrpts that prints a message depeending of the number of arguments passed:
If no arguments are passed to the script, print "No argument"
IF only one arguemnt is passed to the script print "Argument found"
Otherwise, print Argument found
You must use console.log(...) to print all the output
Not allowed to use var
*/

const argsLength = process.argv.length;

if (argsLength < 3) {
  console.log('No argument');
} else if (argsLength === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
