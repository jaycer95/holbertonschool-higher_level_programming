#!/usr/bin/node
if (process.argv[2] === undefined) {
  console.log('Missing size');
} else {
  let line = '';
  for (let i = 0; i < process.argv[2]; i++) {
    for (let j = 0; j < process.argv[2]; j++) {
      line += 'X';
    }
    console.log(line);
    line = '';
  }
}
