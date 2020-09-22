#!/usr/bin/node

const request = require('request');
const arg = process.argv[2];
const URL = 'https://swapi-api.hbtn.io/api/films/' + arg;
let x;
const l = {};
request.get(URL, (err, response, body) => {
  (err) ? console.log(err) : x = JSON.parse(body).characters;
  for (const i of x) {
    request.get(i, (err, response, body) => {
      if (!err) {
        l[i] = JSON.parse(body).name;
        if (Object.values(l).length === x.length) {
          for (const j of x) {
            console.log(l[j]);
          }
        }
      }
    });
  }
});
