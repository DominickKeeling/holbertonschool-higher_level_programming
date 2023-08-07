#!/usr/bin/node
/*
Write a script that prints the title of a Star Wars movie where the episode
number matches a given integer.
The first argument is the movie ID
You must use the Star wars API with the endpoint https://swapi-api.hbtn.io/api/films/:id
You must use the module request
*/

const request = require('request');

// construct url endpoint using movie id
const movieId = process.id [2]
const url = 'https://swapi-api.hbtn.io/api/films/:id';


/* make the api request
using the request module make an HTTP GET request to API URL
*/
request(url, (error, response, body) => {
    if (error) {
        console.error(error);
        return;
    }
/* Hanle the API response using the callback function of the request function
Then parse the JSON response to get the movie details
*/
    const movie = JSON.parse(body);
    console.log(movie.title);
})
