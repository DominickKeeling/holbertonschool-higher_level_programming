#!/usr/bin/node
/*
Write a script that reads and prints the content of a file.
The first argument is the file path
The content of the file msut be read in utf-8
If an error occured diring the reading, print the error object
*/

const fs = require('fs');

const filePath = process.arg[2];

fs.readFile(filePath, 'utf-8', (error, data) => {
    if (error) {
        console.error(error);
        return;
    }
    console.log(data);
});