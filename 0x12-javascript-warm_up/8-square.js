#!/usr/bin/node
// Makes a square

const n = parseInt(process.argv[2]);
if (!isNaN(n)) {
  for (let i = 0; i < n; i++) {
    console.log('X'.repeat(n));
  }
} else {
  console.log('Missing size');
}
