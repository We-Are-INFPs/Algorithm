const fs = require("fs");

const getParsedData = (i) => {
  const input = fs.readFileSync(`./in${i}.txt`, "utf8").toString().split('\n');
  const matrix = input.map((row)=>row.split(' ').map(i=>parseInt(i)).filter(i=>i))
  return matrix;
}

const checkOK = (list) => {
  const set = new Set(list);
  if (set.size !== 9) return false;
  return true;
}

const checkRowAndColumn =  (matrix) => {
  for (let i = 0; i <= 8; i += 1) {
    const isRowOK = checkOK(matrix[i]);
    if (!isRowOK) return isRowOK;

    let columnList = [];
    for (let j = 0; j <= 8; j += 1) {
      columnList.push(matrix[j][i]);
    }
    const isColumnOK = checkOK(columnList);
    if (!isColumnOK) return isColumnOK;
  }
  return true;
}

const checkBox = (matrix) => {
  for (let i = 0; i < 9; i += 3) {
    for (let j = 0; j < 9; j += 3) {
      let boxList = [];
      for (let a = 0; a < 3; a += 1){
        for (let b = 0; b < 3; b += 1) {
          boxList.push(matrix[i+a][i+b])
        }
      }
      const isBoxOK = checkOK(boxList);
      isOK = isBoxOK;
      if (!isBoxOK) return isBoxOK;
    }
  };
  return true;
}

for (let i = 1; i < 6; i += 1) {
 const matrix = getParsedData(i);
 if (!checkRowAndColumn(matrix) || !checkBox(matrix)) {
  console.log('NO');
 } else {
   console.log('YES');
 }
};


