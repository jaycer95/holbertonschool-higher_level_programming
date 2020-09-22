#!/usr/bin/node

const fs = require('fs');
const Name = process.argv[2];
fs.readFile(Name, 'utf-8', (err, about) => {
  (err) ? console.log(err) : console.log(about);
});
