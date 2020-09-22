#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const URL = process.argv[2];
const Name = process.argv[3];
let res;
request.get(URL, (err, response, body) => {
  (err) ? console.log(err) : res = body;
  fs.writeFile(Name, res, 'utf-8', (err) => {
    if (err) {
      console.log(err);
    }
  });
});
