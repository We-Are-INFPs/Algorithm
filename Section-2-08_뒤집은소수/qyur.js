const fs = require("fs");

const isPrime = (N) => {
  if (N < 2) return false;
  for (let i = 2; i < parseInt(N / i) + 1; i += 1) {
    if (N % i === 0) return false;
  }
  return N;
}

const reverse = (num) => {
  const numSplittedArray = num.split("");
  const reversedArray = numSplittedArray.reverse();
  const joinedNum = reversedArray.join("");
  return Number(joinedNum);
}

for (let i = 1; i < 6; i += 1) {
  const input = fs.readFileSync(`./in${i}.txt`, "utf8").toString().split('\n');
  const numberList = input[1].split(' ');

  const primeNumberList = numberList
    .map((num) => reverse(num))
    .map((number) => isPrime(number))
    .filter(i => i);

  console.log(primeNumberList.join(" "));
}