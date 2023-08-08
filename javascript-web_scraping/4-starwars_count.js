#!/usr/bin/node
/*
Write a script that prints the number of movies where the character “Wedge Antilles” is present.
The first argument is the API URL of the Star wars API: https://swapi-api.hbtn.io/api/films/
Wedge Antilles is character ID 18 - your script must use this ID for filtering the result of the API
You must use the module request
*/

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const movieData = JSON.parse(body);
  let count = 0;

  for (let i = 0; i < movieData.results.length; i++) {
    const characterUrls = movieData.results[i].characters;
    if (characterUrls.includes('https://swapi-api.hbtn.io/api/people/18/')) {
      count++;
    }
  }

  console.log(count);
});
