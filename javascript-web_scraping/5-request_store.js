#!/usr/bin/node
/*
Write a script that gets the contents of a webpage and stores it in a file
The first argumetn is the URL to request
The second argument is the file path to store the body response
The file must be  UTF-8 encoded
You must use the module request
*/

const fs = require('fs');
const request = require('request');
request.get(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  }
}).pipe(fs.createWriteStream(process.argv[3]));
