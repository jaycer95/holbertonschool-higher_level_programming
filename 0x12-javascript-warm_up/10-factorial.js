#!/usr/bin/node
function factorial (f) {
  if (f === 0) {
    return 1;
  } else {
    return f * factorial(f - 1);
  }
}

if (process.argv[2] !== undefined) {
  console.log(factorial(parseInt(process.argv[2])));
} else {
  console.log(1);
}
