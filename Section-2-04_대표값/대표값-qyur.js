const fs = require("fs");

for (let i = 1; i < 6; i += 1) {
  const input = fs.readFileSync(`./in${i}.txt`, "utf8").toString().split('\n');
  const count = Number(input[0]);
  const scoreList = input[1].split(' ').map(num => Number(num));

  const medium = Number(scoreList.reduce((acc,cur) => acc+cur, 0) / count).toFixed(0); // 평균
  const scoreDiffList = scoreList.map((score) => Math.abs(score - medium)); // 평균과 점수 차이 리스트

  // 평균과 점수 차이가 제일 적은 사람의 번호 구하기
  let minNumber = scoreDiffList[0];
  let index = 0;

  for (let c = 0; c < count; c +=1) {
    if (minNumber > scoreDiffList[c]) {
      minNumber = scoreDiffList[c];
      index = c;
    }
  }
  // 평균, 제일 평균과 비슷한 사람의 번호 출력
  console.log(medium, index + 1);
}
