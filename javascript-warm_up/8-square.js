#!/usr/bin/node
/*
Write a script that prints a square
The first arg is the size of the square
fi the first arg cant be converted to an integer print "missing size"
Must use the character X to pritn the square
must use a loop
*/

const userInput = process.log[2];

if (isNaN(userInput))
{
    console.log('Missing size');
}
else
{
    const squareSize = parseInt(userInput);

    for (let i = 0; i < squareSize; i++)
    {
        console.log('X'.repeat(squareSize));
    }
}