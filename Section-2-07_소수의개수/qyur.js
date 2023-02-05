const fs = require("fs");

for (let i = 1; i < 6; i += 1) {
  const N = Number(fs.readFileSync(`./in${i}.txt`, "utf8"));

  // N+1 길이의 true로 채워진 에라토스테네스 체를 만든다.
  const EratosFilter = new Array(N+1).fill(true);

  for (let i = 2; i * i <= N; i += 1) {
    if (EratosFilter[i]) { // 소수일 때
      for (let j = i * i; j <= N; j += i) {
        EratosFilter[j] = false; // 소수의 배수는 모두 false처리
      }
    }
  }

  // 0과 1은 제외하고 계산
  console.log(EratosFilter.filter((bool)=>bool).length - 2);
}
