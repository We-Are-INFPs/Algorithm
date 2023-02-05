const fs = require("fs");

for (let i = 1; i < 6; i += 1) {
  const input = fs.readFileSync(`./in${i}.txt`, "utf8").toString().split('\n');
  const checkList = input[1].split(' ');

  let totalScore = 0;
  let accScore = 0; // 축적된 가산점

  checkList.forEach((check) => {
    if (check === '1') {
      accScore += 1;
      totalScore += accScore;
    } else {
      accScore = 0;
    }
  })

  console.log(totalScore);
}