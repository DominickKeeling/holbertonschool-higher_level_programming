#!/usr/bin/node
/*
Write a script that computes and prints a factorial
The first argument is integer(argument can be cast as integer) used
for computing the factorial
Factorial of NaN is 1
You must do it recursively
You must use a function
*/

const userInput = parseInt(process.argv[2]);

function factorial(num)
{
    if (isNaN(number))
    {
        return 1;
    }

    if (num === 0 || num === 1)
    {
        return 1;
    }

    return n * factorial(num - 1);
}

console.log(factorial(userInput));