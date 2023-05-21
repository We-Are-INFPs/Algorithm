const fs = require("fs");

const getParsedData = (i) => {
  const input = fs.readFileSync(`./in${i}.txt`, "utf8").toString().split('\n');
  const N = Number(input[0]);
  const parsedNumberList = input[1].split(' ').map((number)=> Number(number)).filter(n => n);
  return [N, parsedNumberList];
}

for (let i = 1; i < 6; i += 1) {
  const [N, parsedNumberList] = getParsedData(i);
  let flag = true;
  let answer = ''
  let left = 0;
  let right = N - 1;
  let targetNumber = 0;

  while (flag) {
    if (left >= right) {
      break;
    }

    let leftNumber = parsedNumberList[left];
    let rightNumber = parsedNumberList[right];

    if (leftNumber < rightNumber) {
      if (targetNumber < leftNumber) {
        answer += 'L';
        targetNumber = leftNumber;
        left += 1;
        continue;
      }
      if (targetNumber < rightNumber) {
        answer  += 'R';
        targetNumber = rightNumber;
        right -= 1;
        continue;
      }
      break;
    }

    if (rightNumber < leftNumber) {
      if (targetNumber < rightNumber) {
        answer  += 'R';
        targetNumber = rightNumber;
        right -= 1;
        continue;
      }
      if (targetNumber < leftNumber) {
        answer += 'L';
        targetNumber = leftNumber;
        left += 1;
        continue;
      }
      break;
    }
  }
  console.log(answer,'answer');
}
