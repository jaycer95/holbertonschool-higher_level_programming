#!/usr/bin/node

const request = require('request');
const URL = process.argv[2];
let res = [];
request.get(URL, (err, response, body) => {
  (err) ? console.log(err) : res = JSON.parse(body).results;
  let count = 0;
  for (const i of res) {
    for (const j of i.characters) {
      if (j.includes('/18')) {
        count += 1;
      }
    }
  }
  console.log(count);
});
