#!/usr/bin/node
/*
Write a script that prints the number of movies where the character “Wedge Antilles” is present.
The first argument is the API URL of the Star wars API: https://swapi-api.hbtn.io/api/films/
Wedge Antilles is character ID 18 - your script must use this ID for filtering the result of the API
You must use the module request
*/

const request = require('request');

const apiUrl = process.argv[2];
const characterId = 18;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const films = JSON.parse(body).results;
  const count = films.reduce((total, film) => {
    if (film.characters.includes(`https://swapi-api.hbtn.io/api/people/${characterId}/`)) {
      return total + 1;
    }
    return total;
  }, 0);
  console.log(count);
});