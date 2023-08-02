#!/usr/bin/node
/*
Write a scripts that prints the first argument passed to it:
if no arguments are passed to the script print 'No argument'
you must use console.log(...) to print all output
you are not allowed to use var
you are not allowed to use lengnth
*/

if (!process.argv[2]) {
    console.log('No argument');
  } else {
    console.log(process.arg[2]);
  }
