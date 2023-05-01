const fs = require("fs");

const getParsedData = (i) => {
  const input = fs.readFileSync(`./in${i}.txt`, "utf8").toString().split('\n');
  const matrix = input.map((row)=>row.split(' ').map(i=>parseInt(i)).filter(i=>i))
  return matrix;
}

for (let i = 1; i < 6; i += 1) {
 const matrix = getParsedData(i);
 let countHwemoon = 0;
 for (let i = 0; i < 7; i += 1) {
  for (let j =0; j < 3; j += 1) {
    if (matrix[i][j] === matrix[i][j+4] && matrix[i][j+1] === matrix[i][j+3]) {
      countHwemoon += 1;
    }
    if (matrix[j][i] === matrix[j+4][i] && matrix[j+1][i] === matrix[j+3][i]) {
      countHwemoon += 1;
    }
  }
 }

 console.log(countHwemoon);
};
