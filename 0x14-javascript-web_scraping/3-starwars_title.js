#!/usr/bin/node

const request = require('request');
const mId = process.argv[2];
const URL = 'https://swapi-api.hbtn.io/api/films/' + mId;
request(URL, (err, response, body) => {
  (err) ? console.log(err) : console.log(JSON.parse(body).title);
});
