#!/usr/bin/node

/*
Write a script that writes a string to a file
The first argument is the file path
The second argument is the string to write
The content must be written in utf-8
If an error occurred during while writting, print the error object
*/

const fs = require('fs');

const filePath = process.arg[2];
const content = process.arg[3];

fs.writeFile(filePath, content, 'utf-8', (error) => {
    if (error) {
        console.error(error);
    }
})