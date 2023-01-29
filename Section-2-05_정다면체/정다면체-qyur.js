const fs = require("fs");

for (let i = 1; i < 6; i += 1) {
  const [N, M] = fs.readFileSync(`./in${i}.txt`, "utf8").toString().split(' ');

  const sumNumberCountObject = {};
  for (let n = 1; n < Number(N) + 1; n += 1) {
    for (let m = 1; m < Number(M) + 1; m += 1) {
      const targetKey = String(n + m);
      const targetValue = sumNumberCountObject[targetKey];
      sumNumberCountObject[targetKey] = targetValue ? targetValue + 1 : 1;
    }
  }

  const maxCount = Math.max(...Object.values(sumNumberCountObject));

  let result = ''
  Object.entries(sumNumberCountObject)
  .forEach(([ key, value ])=>{
    if (value === maxCount) {
      result = result + ' ' + key;
    }
  })

  console.log(result);
}