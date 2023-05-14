const fs = require("fs");

const getParsedData = (i) => {
  const input = fs.readFileSync(`./in${i}.txt`, "utf8").toString().split('\n');
  const [N, M] = input[0].split(' ').map((number)=> Number(number));
  const parsedNumberList = input[1].split(' ').map((number)=> Number(number)).filter(n => n)
  return [N, M, parsedNumberList];
}

const binarySeacrh = (M, parsedNumberList) => {
  let start = 0;
  let end = parsedNumberList.length - 1;
  let mid;

  while (start <= end) {
   mid = parseInt((start + end)/2);

   if (M === parsedNumberList[mid]) {
     return mid;
   }

   if (M < parsedNumberList[mid]) {
    end = mid - 1;
   }

   if (M > parsedNumberList[mid]) {
     start = mid + 1;
   }
  }
}

for (let i = 1; i < 6; i += 1) {
 const [N, M, parsedNumberList] = getParsedData(i)
 parsedNumberList.sort((a,b)=>a-b);

 const resultIndex = binarySeacrh(M, parsedNumberList);

 console.log(resultIndex + 1);
}