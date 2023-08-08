#!/usr/bin/node
/*
Write a script that reads and prints the content of a file.
The first argument is the file path
The content of the file msut be read in utf-8
If an error occured diring the reading, print the error object
*/

const fileReader = require('fs');

const myTargetFile = process.argv[2];

fileReader.readFile(myTargetFile, 'utf8', function (err, data) {
  if (err) {
    console.log(err); // Log the error if reading fails
  } else {
    console.log(data); // Log the content of the file if reading is successful
  }
});
