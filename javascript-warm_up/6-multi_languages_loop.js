#!/usr/bin/node
/*
Write a script that prints 3 lines: (like 1-multi_languages.js) but 
by using an array of string and a loop
The first line: "C is fun"
the second line: "Python is cool"
The third line: "Javascript is amazing"
You are not allowed to use any if/else statements
You can only use one console.log
You must use a loop (while, for, etc)
*/
const myArr = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
for (let x = 0; x < myArr.length; x++) {
  console.log(myArr[x]);
}
