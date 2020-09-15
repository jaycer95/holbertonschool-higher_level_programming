#!/usr/bin/node
if (process.argv[2] === undefined) {
  console.log('Missing size');
} else {
  let k = [];
  let s = '';
  for (let i = 0; i < process.argv[2]; i++) {
    for (let j = 0; j < process.argv[2]; j++) {
      s += 'X';
    }
    k[i] = s;
    s = '';
  }
  console.log(k.join('\n'));
}
