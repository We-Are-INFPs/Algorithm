const fs = require("fs");

const getParsedData = (i) => {
  const input = fs.readFileSync(`./in${i}.txt`, "utf8").toString().split('\n');
  const N = input.splice(0,1);
  const first= input.splice(0,N[0]);
  const M = input.splice(0,1);
  const firstMatrix = first.map((row)=>row.split(' ').map(i=>parseInt(i)).filter(i=>i === 0 || i))
  const secondMatrix = input.map((row)=>row.split(' ').map(i=>parseInt(i)).filter(i=>i === 0 || i))
  return [N[0], firstMatrix, M[0], secondMatrix];
}

for (let i = 1; i < 6; i += 1) {
 const [N, firstMatrix, M, secondMatrix] = getParsedData(i);
 // 회전
 secondMatrix.forEach(([rowIndex, direction, number])=>{
  const realNumber = number % N;
  const realRowIndex = rowIndex -1;
  const targetRow = firstMatrix.splice(realRowIndex, 1)[0];

  if (direction === 0) {
    const splicedNumbers = targetRow.splice(0,realNumber);
    firstMatrix.splice(realRowIndex,0,[...targetRow, ...splicedNumbers]);
  }
  if (direction === 1) {
    const splicedNumbers = targetRow.splice(-realNumber);
    firstMatrix.splice(realRowIndex,0,[...splicedNumbers, ...targetRow]);
  }
 })
 // 총합
 const half = parseInt(N/2);
 let totalSum = 0;
 for (let i = 0; i < N; i +=1) {
  const diff = Math.abs(half - i);
  for (let j = half - diff; j <= half + diff; j += 1){
    totalSum += firstMatrix[i][j];
  }
 }

 console.log(totalSum);
}
