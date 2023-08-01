#!/usr/bin/node
/*
Write a scrpts that prints a message depeending of the number of arguments passed:
If no arguments are passed to the script, print "No argument"
IF only one arguemnt is passed to the script print "Argument found"
Otherwise, print Argument found
You must use console.log(...) to print all the output
Not allowed to use var
*/

const numArgs = process.argv.length -2;

if (numArgs === 0)
{
    console.log('No argument');
}
else if (numArgs === 1)
{
    console.log('Argument found');
}
else
{
    console.log('Argument found');
}
    
console.log();
