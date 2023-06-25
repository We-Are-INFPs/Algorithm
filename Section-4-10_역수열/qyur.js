const fs = require("fs");

const getParsedData = (i) => {
  const input = fs.readFileSync(`./in${i}.txt`, "utf8").toString().split('\n');
  const [N] = input[0].split(' ').map((number)=> Number(number));
  const parsedNumberList = input[1].split(' ').map((number)=> Number(number)).filter(n => !isNaN(n))
  return [N, parsedNumberList];
}

const getNewTargetArray = (targetArray, targetNumber, targetCount) => {
 let biggerCount = 0;
 let index = -1;

 targetArray.forEach((number, idx)=>{
  if (biggerCount === targetCount) {
    index = idx
  }
  if (number > targetNumber) {
    biggerCount += 1;
  }
 })

 targetArray[index] = targetNumber;
 return targetArray;
}

for (let i = 1; i < 6; i += 1) {
 const [N, parsedNumberList] = getParsedData(i)
 let targetArray = new Array(N).fill(N+1);

 for (let i = 0; i < N; i += 1) {
  targetArray = getNewTargetArray(targetArray, i+1, parsedNumberList[i]);
 }

 console.log(targetArray);
}