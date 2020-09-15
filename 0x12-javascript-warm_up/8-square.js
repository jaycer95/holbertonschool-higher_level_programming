#!/usr/bin/node
if (isNaN(parseInt(process.argv[2], 10)) === false) {
  let line = '';
  for (let i = 0; i < process.argv[2]; i++) {
    for (let j = 0; j < process.argv[2]; j++) {
      line += 'X';
    }
    console.log(line);
    line = '';
  }
} else {
  console.log('Missing size')
}
