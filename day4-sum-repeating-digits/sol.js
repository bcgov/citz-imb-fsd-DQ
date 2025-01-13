const inputString = "";

const input = Array.from(inputString);
console.log(input);
console.log(typeof input);
console.log(typeof input[0]);

const increasedTimes = input.reduce(
	(acc, curr, index, arr) => (curr > arr[index - 1] ? acc + 1 : acc),
	0,
);

console.log(increasedTimes);
