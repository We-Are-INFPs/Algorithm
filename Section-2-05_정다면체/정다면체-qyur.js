const fs = require("fs");

// [1,2,3,4 .. ] 연속되는 숫자를 가진 array를 만드는 함수
const makeOrderedList = (number) => {
  let orderedList = [];
  for (let i = 1; i < Number(number) + 1; i += 1) {
    orderedList.push(i);
  }
  return orderedList;
}

for (let i = 1; i < 6; i += 1) {
  const [N, M] = fs.readFileSync(`./in${i}.txt`, "utf8").toString().split(' ');
  let NList = makeOrderedList(N);
  let MList = makeOrderedList(M);

  // 숫자의 합을 sumNumberCountObject에 저장
  const sumNumberCountObject = {};
  NList.forEach((NNumber) => {
    MList.forEach((MNumber) => {
      const targetKey = String(NNumber + MNumber);
      const targetValue = sumNumberCountObject[targetKey];
      sumNumberCountObject[targetKey] = targetValue ? targetValue + 1 : 1;
    })
  })

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