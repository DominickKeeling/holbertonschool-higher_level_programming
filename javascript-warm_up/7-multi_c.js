#!/usr/bin/node
/*
Write a script that prints x times "C is fun"
Where x is the first argument of the script
if the first argument cant be converted to an integer, pritn "Missing number
of occurences"
Must use a loop (while, for, etc)
*/

const input = process.argv[2];

if (isNaN(input))
{
    console.log('Missing number of occurences')
}
const numberOfOccurrences = parse(input);

for(let i = 0; i < numberOfOccurrences; i++)
{
    console.log('C is fun');
}
