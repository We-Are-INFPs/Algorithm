const fs = require("fs");

const getParsedData = (i) => {
  const input = fs.readFileSync(`./in${i}.txt`, "utf8").toString().split('\n');
  const [targetNumber, M] = input[0].split(' ');
  return [targetNumber, M]
}

const findNumberIndex = (parsedNumberList) => {
  for (let i = 0; i < parsedNumberList.length; i += 1) {
    if (parsedNumberList[i] < parsedNumberList[i+1]) {
      return i;
    }
  }
  // 제일 마지막 숫자가 제일 작은 경우
  return parsedNumberList.length - 1;
 }

for (let i = 1; i < 6; i += 1) {
 let [parsedNumber, M] = getParsedData(i);
 const parsedNumberList = parsedNumber.split('').map((n)=>Number(n));

 while (M) {
  parsedNumberList.splice(findNumberIndex(parsedNumberList), 1);
  M -= 1;
 }

 console.log(parsedNumberList.join(''));
}
