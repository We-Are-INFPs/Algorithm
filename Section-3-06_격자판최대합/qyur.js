const fs = require("fs");

const getParsedData = (i) => {
  const input = fs.readFileSync(`./in${i}.txt`, "utf8").toString().split('\n');
  const N = input.splice(0,1);
  const matrix = input.map((row)=>row.split(' ').map(i=>parseInt(i)).filter(i=>i))
  return [N[0], matrix];
}

for (let i = 1; i < 6; i += 1) {
 const [matrixLength, matrix] = getParsedData(i);
 let columnMax = 0; // 열 최대
 let rowMax = 0; // 행 최대
 let crossSum1 = 0; // 대각선 왼쪽 -> 오른쪽 총합
 let crossSum2 = 0; // 대각선 오른쪽 -> 왼쪽 총합

 for (let i = 0; i < matrixLength; i+= 1) {
  let columnSum = 0;
  let rowSum = 0;

  crossSum1 += matrix[i][i];
  crossSum2 += matrix[i][matrixLength-1-i];

  for (let j = 0; j < matrixLength; j+= 1) {
    rowSum += matrix[i][j];
    columnSum += matrix[j][i];
  }
  if (rowMax < rowSum) {
    rowMax = rowSum;
  }
  if (columnMax < columnSum) {
    columnMax = columnSum;
  }
 }

 console.log(Math.max(rowMax, columnMax, crossSum1, crossSum2));
}