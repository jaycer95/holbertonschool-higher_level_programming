#!/usr/bin/node

const request = require('request');
const arg = process.argv[2];
const URL = 'https://swapi-api.hbtn.io/api/films/' + arg;
let res = [];
request.get(URL, (err, response, body) => {
  (err) ? console.log(err) : res = JSON.parse(body).characters;
  for (const i of res) {
    request.get(i, (err, response, body) => {
      (err) ? console.log(err) : console.log(JSON.parse(body).name);
    });
  }
});
