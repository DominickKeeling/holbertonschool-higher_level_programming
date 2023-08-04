#!/usr/bin/node

/*
Write a script that displays the status code of a GET request
The first argument is the URL to request (GET)
The status code must be printed like this: code: <status code>
You must use the module request
*/

const request = require('request');

const url = process.arg[2];

request(url, (error, response) => {
    if (error) {
        console.error(error);
        return;
    }
    console.log('code: ${response.statusCode}');
})