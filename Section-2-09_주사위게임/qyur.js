const fs = require("fs");

const countSameNumber = (numbers) => {
  let count = 0;
  let num = 0;

  const [first, second, third] = numbers;
  if (first === second) {
    count += 1;
    num = first;
  }
  if (second === third) {
    count += 1;
    if (num < second) {
      num = second;
    }
  }
  if (third === first) {
    count += 1;
    if (num < third) {
      num = third;
    }
  }
  if (count === 0) {
    num = Math.max(...numbers);
  }

  return [count, num];
}

const firstRule = (number) => 10000 + number*1000;
const secondRule = (number) => 1000 + number*100;
const thirdRule = (number) => number*100;

for (let i = 1; i < 6; i += 1) {
  const input = fs.readFileSync(`./in${i}.txt`, "utf8").toString().split('\n');
  input.splice(0,1);

  let bestPrice = 0;
  let maxCount = 0;
  let maxNum = 0;
  input.forEach(a=>
    {
      const numberList = a.split(' ');
      numberList.pop();
      const numbers = numberList.map(n => n && Number(n));

      if (numbers.length !== 3) return null;

      const [count, num] = countSameNumber(numbers);

      if (maxCount < count) {
        maxCount = count;
      }
      if (maxNum < num) {
        maxNum = num;
      }
    }
  );

  switch (maxCount) {
    case 3:
      calculation = firstRule(maxNum);
      break;
    case 1:
      calculation = secondRule(maxNum);
      break;
    case 0:
      calculation = thirdRule(maxNum);
  }

  if (bestPrice < calculation) {
    bestPrice = calculation;
  }


  console.log(bestPrice);
}