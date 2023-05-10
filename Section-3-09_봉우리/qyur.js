const fs = require("fs");

const getParsedData = (i) => {
  const input = fs.readFileSync(`./in${i}.txt`, "utf8").toString().split('\n');
  const N = input.splice(0,1);
  const matrix = input.map((row)=>row.split(' ').map(i=>parseInt(i)).filter(i=>i))
  return [N[0], matrix];
}

const dx = [0, 1, 0, -1];
const dy = [1, 0, -1, 0];

const getMaxAroundNumber = (matrix, i, j) => {
  let maxAroundNumber = 0;
  for (let d = 0; d < 4; d += 1){
    const xDirection = i + dx[d];
    const yDirection = j + dy[d];
    if (xDirection < 0 || yDirection < 0 || xDirection >= matrix.length || yDirection >= matrix.length) {
      continue;
    }
    const aroundNumber = matrix[xDirection][yDirection];
    if (aroundNumber > maxAroundNumber) {
      maxAroundNumber = aroundNumber;
    }
  }
  return maxAroundNumber;
}

for (let i = 1; i < 6; i += 1) {
 const [N, matrix] = getParsedData(i);
 let top = 0;
 for (let i = 0; i < N; i += 1) {
  for (let j = 0; j < N; j += 1) {
    const target = matrix[i][j];
    const maxAroundNumber = getMaxAroundNumber(matrix, i, j);
    if (target > maxAroundNumber) {
      top += 1;
    }
  }
 }
 console.log(top);
};


