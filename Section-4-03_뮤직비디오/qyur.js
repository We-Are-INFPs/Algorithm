const fs = require("fs");

const getParsedData = (i) => {
  const input = fs.readFileSync(`./in${i}.txt`, "utf8").toString().split('\n');
  const [N, M] = input[0].split(' ').map((number)=> Number(number));
  const parsedNumberList = input[1].split(' ').map((number)=> Number(number)).filter(n => n)
  return [N, M, parsedNumberList];
}

const getTotalCount = (mid, parsedNumberList) => {
  let count = 1;
  let sum = 0;
  parsedNumberList.forEach((n)=>{
    if (sum + n > mid) {
      count += 1;
      sum = n;
    } else {
      sum += n;
    }
  })
  return count;
}

for (let i = 1; i < 6; i += 1) {
 const [N, M, parsedNumberList] = getParsedData(i)
 let min = 1;
 let max = parseInt(parsedNumberList.reduce((acc,cur)=>acc+cur, 0));
 let total = 0;

 while (min <= max) {
  let mid = parseInt((min+max)/2);
  if (getTotalCount(mid, parsedNumberList) <= M) {
    max = mid - 1;
    total = mid;
  } else {
    min = mid + 1;
  }
 }

 console.log(total);
}