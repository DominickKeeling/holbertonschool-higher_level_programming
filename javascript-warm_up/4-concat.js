#!/usr/bin/node
/*
Write a script that prints two arguments passed to it in the 
following format: "is"
You must use console.log()
Not allowed to use var
*/

const arg1 = process.argv[2];
const arg2 = process.argv[3];

console.log('${arg1} is ${arg2}');
