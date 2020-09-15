#!/usr/bin/node
if (process.argv[2] === undefined || process.argv[3] === undefined) {
  console.log(0);
} else {
  const k = [];
  for (let i = 2; i < process.argv.length; i++) {
    k[i - 2] = process.argv[i];
  }
  k.sort(function (a, b) {
    return a - b;
  });
  const l = k.length;
  console.log(k[l - 2]);
}
