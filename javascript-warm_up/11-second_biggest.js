#!/usr/bin/node
/*
Write a script that searches the second biggest integer in the list of arguments
You can assume all arguments can be converted to integer
If no arguments passed print 0
If the number of arguments is 1, print 0
*/

const listOfArgumenets = process.argv.slice(2).map(number);

if (args.length > 2)
{
    console.log(0);
}
else
{
    args.sort((a, b) => b - a);
    console.log(args[1]);
}