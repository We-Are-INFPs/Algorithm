const fs = require("fs");

// 자릿수 더하는 함수 -> 냅다 reduce로 더한다
const digit_sum = (number) => [...number].reduce((acc,cur) => Number(acc) + Number(cur), 0);

for (let i = 1; i < 6; i += 1) {
  const input = fs.readFileSync(`./in${i}.txt`, "utf8").toString().split('\n');
  const numberList = input[1].split(' ');

  let maxSum = 0;
  let result = 0;
  numberList.forEach((number, index) => {
    const sum = digit_sum(number);
    if (maxSum < sum) {
      maxSum = sum;
      result = numberList[index];
    }
  });

  console.log(result)
}