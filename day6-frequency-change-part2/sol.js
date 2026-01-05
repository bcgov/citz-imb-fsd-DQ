const fs = require("fs");

const t0 = performance.now();

const input_string = fs.readFileSync("./input.txt", { encoding: "utf-8" });

const changes = input_string.split(/\r?\n/).map(line => Number(line.trim()));

function repeatedFreq(changes) {
  const seen_frequency = new Set();
  let frequency = 0;
  seen_frequency.add(frequency);

  // Repeat the sequence
  while (true) {
    for (const change of changes) {
      // frequency += Number(change);
      if (seen_frequency.has(change)) {
        return change;
      } else {
        seen_frequency.add(change);
      }
    }
  }
}

console.log(repeatedFreq(changes));

const t1 = performance.now();
console.log(t1 - t0, " ms");



// const fs = require("fs");

// const start = Date.now()
// const t0 = performance.now();
// const input_string = fs.readFileSync("./input.txt", { encoding: "utf-8" });

// const changes = input_string.split(/\r?\n/).filter(line => line.trim() !== "");

// console.log(changes.reduce((sum, change) => sum + Number(change), 0));

// const t1 = performance.now();
// console.log(Date.now() - start);

// console.log(t1 - t0);
