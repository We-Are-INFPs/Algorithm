const fs = require("fs");

const getParsedData = (i) => {
  const input = fs.readFileSync(`./in${i}.txt`, "utf8").toString().split('\n');
  const [N] = input[0].split(' ').map((number)=> Number(number));
  const parsedNumberList = input[1].split(' ').map((number)=> Number(number)).filter(n => n);
  const M = Number(input[2]);
  return [N, M, parsedNumberList];
}

for (let i = 1; i < 6; i += 1) {
 const [N, M, parsedNumberList] = getParsedData(i);
 let boxList = [...parsedNumberList];
 let count = M;

 while (count > 0) {
  count -= 1;
  let minNum = 100;
  let maxNum = 0;
  let minIdx = -1;
  let maxIdx = -1;
  boxList.forEach((number, index)=>{
    if (number < minNum) {
      minNum = number;
      minIdx = index;
    }
    if (number > maxNum) {
      maxNum = number;
      maxIdx = index;
    }
  })
  boxList.splice(minIdx, 1, boxList[minIdx] + 1);
  boxList.splice(maxIdx, 1, boxList[maxIdx] - 1);
 }
 console.log(Math.max(...boxList) - Math.min(...boxList));
}