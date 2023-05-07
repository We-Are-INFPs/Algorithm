const fs = require("fs");

const getParsedData = (i) => {
  const input = fs.readFileSync(`./in${i}.txt`, "utf8").toString().split('\n');
  const [K, N] = input[0].split(' ').map((number)=> Number(number));
  const numbers = input.splice(1);
  const parsedNumberList = numbers.filter(n=>n).map((num) => parseInt(num));
  return [K, N, parsedNumberList];
}

const getTotalCount = (parsedNumberList, mid) => {
  let totalCount = 0;
  parsedNumberList.forEach((num)=>{
    totalCount += parseInt(num / mid);
  })
  return totalCount;
}

for (let i = 1; i < 6; i += 1) {
 const [K, N, parsedNumberList] = getParsedData(i)
 parsedNumberList.sort();
 let max = parseInt(parsedNumberList.reduce((acc,cur)=>acc+cur, 0) / N);
 let min = 1;
 while (min <= max) {
  let mid = parseInt((max+min)/2);
  if (getTotalCount(parsedNumberList, mid) >= N) {
    min = mid + 1;
  } else {
    max = mid - 1;
  }
 }
 console.log(max);
}