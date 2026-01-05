const fs = require("fs");

const start = Date.now()
const t0 = performance.now();
const input_string = fs.readFileSync("./input.txt", { encoding: "utf-8" });

const changes = input_string.split(/\r?\n/).filter(line => line.trim() !== "");

console.log(changes.reduce((sum, change) => sum + Number(change), 0));

const t1 = performance.now();
console.log(Date.now() - start);

console.log(t1 - t0);
