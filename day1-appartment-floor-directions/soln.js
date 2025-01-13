const main = (input) => {
	if (typeof input !== "string") return null;
	let floor = 0;
	for (let i = 0; i <= input.length; i++) {
		if (input[i] === "(") floor++;
		if (input[i] === ")") floor--;
	}
	return floor;
};

const chatGPT = (str) => {
	return str.split("").reduce((acc, char) => {
		return acc + (char === "(" ? 1 : char === ")" ? -1 : 0);
	}, 0);
};
const input = "";
console.log(chatGPT(input));
