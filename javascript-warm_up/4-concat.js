#!/usr/bin/node
/*
Write a script that prints two arguments passed to it in the 
following format: "is"
You must use console.log()
Not allowed to use var
*/

const Args = process.argv.slice(2);
console.log('%s is %s', Args[0], Args[1]);
