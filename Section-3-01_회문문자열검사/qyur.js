const fs = require("fs");

for (let i = 1; i < 6; i += 1) {
  const input = fs.readFileSync(`./in${i}.txt`, "utf8").toString().split('\n');
  const N = input.splice(0,1);

  input.forEach((t,index) => {
    const text = t.trim().toLowerCase();
    const middle =  parseInt(text.length / 2);
    const firstPart = text.slice(0, middle);
    const secondPart = text.slice(-middle).split("").reverse().join(""); // 배열 생성 -> 배열 뒤집기 -> string으로 join
    if (firstPart === secondPart) {
      console.log(`#${index+1} YES`);
    } else {
      console.log(`#${index+1} NO`);
    }
  })
}