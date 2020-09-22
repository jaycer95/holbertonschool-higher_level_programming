#!/usr/bin/node

const request = require('request');
const URL = process.argv[2];
let a;
const res = {};
request.get(URL, (err, response, body) => {
  (err) ? console.log(err) : a = JSON.parse(body);
  for (const i of a) {
    if (i.completed === true) {
      if (res[i.userId]) {
        res[i.userId] += 1;
      } else {
        res[i.userId] = 1;
      }
    }
  }
  console.log(res);
});
