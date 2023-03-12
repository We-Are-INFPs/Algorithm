const fs = require("fs");

const getParsedData = (i) => {
  const input = fs.readFileSync(`./in${i}.txt`, "utf8").toString().split('\n');
  const targetSum = input[0].split(' ')[1];
  const parsedNumberList = input[1].split(' ').map((number)=> Number(number)).filter(n => n)
  return [Number(targetSum), parsedNumberList]
}

for (let i = 1; i < 6; i += 1) {
 const [targetSum, numberList] = getParsedData(i)

 let count = 0;

 for (let i = 0; i < numberList.length; i += 1) {
  let tempSum = numberList[i];
  if (tempSum > targetSum) break;
  if (tempSum === targetSum) {
    count += 1;
    break;
  }
  // 해당 인덱스의 숫자와 인덱스 뒤의 숫자들을 더하는 for 문을 돌다가
  // 더한 숫자(tempSum)가 targetSum보다 커지거나 같아지면 break;
  for (let j = i + 1; j < numberList.length; j += 1) {
    tempSum = tempSum + numberList[j];
    if (tempSum > targetSum) break;
    if (tempSum === targetSum) {
      count += 1;
      break;
    }
  }
 }
 console.log(count);
}