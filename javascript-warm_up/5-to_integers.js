#!/usr/bin/node
/*
Write a script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer:
If the argument can’t be converted to an integer, print “Not a number”
You must use console.log(...) to print all output
You are not allowed to use var
You are not allowed to use try/catch
*/

const inValue = process.argv[2];
if (isNaN(inValue)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(inValue));
}
