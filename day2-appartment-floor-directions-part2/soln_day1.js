const main = (input) => {
	if (typeof input !== "string") return null;
	let floor = 0;
	let basement = undefined;
	for (let i = 0; i <= input.length; i++) {
		if (input[i] === "(") floor++;
		if (input[i] === ")") floor--;
		if (!basement && floor === -1) basement = i;
		//if (!basement && floor === -1) basement === i
		//if (floor === -1) basement ??= i
	}
	return [floor, basement];
};

const chatGPT = (str) => {
	return str.split("").reduce((acc, char) => {
		return acc + (char === "(" ? 1 : char === ")" ? -1 : 0);
	}, 0);
};

const input = "";

console.log(main(input));
//console.log(chatGPT(input))
