const fs = require("fs");

const getParsedData = (i) => {
  const input = fs.readFileSync(`./in${i}.txt`, "utf8").toString().split('\n');
  const N = input.splice(0,1);
  const matrix = input.map((row)=>row.split(' ').map(i=>parseInt(i)).filter(i=>i))
  return [N[0], matrix];
}

for (let i = 1; i < 6; i += 1) {
 const [matrixLength, matrix] = getParsedData(i);
 const half = parseInt(matrixLength / 2);
 let AppleSum = 0;

 for (let i = 0; i < matrixLength; i += 1) {
  const diff = Math.abs(half - i); // 중앙 인덱스와의 차이
  for (let j = diff; j <= half + half - diff; j += 1) {
    AppleSum += matrix[i][j];
  }
};

console.log(AppleSum);
}
