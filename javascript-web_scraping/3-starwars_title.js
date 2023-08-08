#!/usr/bin/node
/*
Write a script that prints the title of a Star Wars movie where the episode
number matches a given integer.
The first argument is the movie ID
You must use the Star wars API with the endpoint https://swapi-api.hbtn.io/api/films/:id
You must use the module request
*/

const request = require('request');

const movieId = process.argv[2];

const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }

  const data = JSON.parse(body);

  console.log(`${data.title}`);
});
