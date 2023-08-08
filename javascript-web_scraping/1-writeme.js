#!/usr/bin/node

/*
Write a script that writes a string to a file
The first argument is the file path
The second argument is the string to write
The content must be written in utf-8
If an error occurred during while writting, print the error object
*/

const fileReader = require('fs');

const myTargetFile = process.argv[2];
const myContent = process.argv[3];

fileReader.writeFile(myTargetFile, myContent, 'utf8', function (err) {
  if (err) {
    console.log(err); // Log the error if writing fails
  }
});
